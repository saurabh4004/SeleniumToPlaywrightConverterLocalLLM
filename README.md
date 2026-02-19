# 🚀 Selenium to Playwright Converter (Local LLM)

A powerful, privacy-focused tool that automatically converts legacy **Selenium Java (TestNG)** test scripts into modern **Playwright TypeScript** code using a **Local LLM** (Ollama + CodeLlama).

![UI Screenshot](https://via.placeholder.com/800x400?text=Selenium+to+Playwright+Converter+UI)

## ✨ Features

- **Zero Data Leakage:** Runs entirely on your local machine using Ollama. No code leaves your network.
- **Intelligent Conversion:**
    - Converts `driver.findElement(By.id(...))` to `page.locator(...)` or `page.getBy...`.
    - Translates TestNG annotations (`@Test`, `@BeforeClass`) to Playwright test hooks.
    - Handles assertions (`Assert.assertEquals` -> `expect(...).toHaveText`).
- **Modern UI:** Clean, dark-mode interface with syntax highlighting and real-time status.
- **Auto-Formatting:** stripping conversational filler to give you pure, ready-to-run code.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

1.  **Python 3.8+** (for the backend server).
2.  **Ollama**: Download from [ollama.com](https://ollama.com).
3.  **CodeLlama Model**: Run the following command in your terminal to pull the model:
    ```bash
    ollama pull codellama
    ```

## 📦 Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/saurabh4004/SeleniumToPlaywrightConverterLocalLLM.git
    cd SeleniumToPlaywrightConverterLocalLLM
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

The project requires two terminal windows to run (Backend + Frontend).

### Step 1: Start the Backend (API)
In terminal #1:
```bash
python -m uvicorn backend.server:app --reload --port 8000
```

### Step 2: Start the Frontend (UI)
In terminal #2:
```bash
python -m http.server 8080 --directory frontend
```

### Step 3: Convert Code
1.  Open your browser and navigate to: **[http://localhost:8080](http://localhost:8080)**
2.  Paste your Selenium Java code into the left pane.
3.  Click **"⚡ Convert Code"**.
4.  Wait for the Local LLM to process (1st run may take 1-2 mins to load the model).
5.  Copy the generated Playwright code from the right pane.

## ⚠️ Troubleshooting

-   **Conversion is slow / "Hanging":**
    -   CodeLlama is a large model (3.8GB+). On CPU-only machines, it can take time to load.
    -   **Fix:** Check the timer in the UI. If it's counting, it's working.
    -   **Tip:** Run `ollama run codellama "hi"` in your terminal before starting the app to pre-warm the model.

-   **"Network Error" or Connection Issues:**
    -   Ensure Ollama is running (`ollama serve`).
    -   Ensure the backend server is running on port 8000.

## 🏗️ Architecture

```mermaid
graph TD
    User[User] -->|Pastes Java Code| UI[Frontend (HTML/JS)]
    UI -->|POST /convert| API[Backend (FastAPI)]
    
    subgraph "Core Engine"
    API -->|Load SOP| SOP[System Prompt SOP]
    API -->|Construct Prompt| LLM_Client[LLM Client]
    LLM_Client -->|Query| Ollama[Ollama (Local LLM)]
    Ollama -->|Response| LLM_Client
    end
    
    LLM_Client -->|Cleaned Code| API
    API -->|Save File| FileSys[Output Directory]
    API -->|JSON Response| UI
    UI -->|Display Code| User
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style UI fill:#bbf,stroke:#333,stroke-width:2px
    style API fill:#dfd,stroke:#333,stroke-width:2px
    style Ollama fill:#fdd,stroke:#333,stroke-width:2px
```

-   **Frontend:** HTML5, CSS3 (Dark Mode), Vanilla JS.
-   **Backend:** FastAPI (Python).
-   **AI Engine:** Ollama (CodeLlama).
-   **Protocol:** [B.L.A.S.T.](B.L.A.S.T.md) (Blueprint, Link, Architect, Stylize, Trigger).

## 📄 License

MIT License. Free to use and modify.
