# Project Constitution (Gemini) - Selenium to Playwright Converter

## 1. Vision
**North Star:** A web-based "Selenium to Playwright Converter" that allows users to input Selenium Java (TestNG) code and receive highly readable, idiomatic Playwright (TypeScript/JavaScript) code. The system uses a Local LLM (Ollama) to perform intelligent conversion, displaying the result in the UI and saving it to a local directory.

## 2. Data Schemas

### Input Payload (Frontend -> Backend)
```json
{
  "source_code": "string (The raw Selenium Java code)",
  "output_filename": "string (Desired filename, e.g., 'login.spec.ts')",
  "target_language": "string ('typescript' | 'javascript')"
}
```

### Output Payload (Backend -> Frontend)
```json
{
  "success": "boolean",
  "converted_code": "string (The generated Playwright code)",
  "file_path": "string (Absolute path where file was saved)",
  "message": "string (Status or error message)"
}
```

## 3. Behavioral Rules
1.  **Readability Over Strictness:** Do not produce a line-by-line literal translation if it compromises readability. Use Playwright's best practices (e.g., `await expect(locator).toBeVisible()` instead of generic assertions).
2.  **TestNG to Playwright Mapping:**
    - `@Test` -> `test('name', async ({ page }) => { ... })`
    - `@BeforeMethod` -> `test.beforeEach(async ({ page }) => { ... })`
    - `@AfterMethod` -> `test.afterEach(async ({ page }) => { ... })`
    - `@BeforeClass` -> `test.beforeAll(...)`
    - `@AfterClass` -> `test.afterAll(...)`
3.  **Locators:** Intelligently convert `By.xpath`, `By.id`, etc. to `page.locator()`, favoring user-facing locators (text, label, role) if inferable, otherwise stick to reliable selectors.
4.  **Output:** Always display the code in the UI *and* save it to the specified output directory.

## 4. Architectural Invariants
- **Core Engine:** Python + Local LLM (Ollama).
- **Frontend:** Modern HTML/CSS/JS (Rich Aesthetics).
- **Communication:** HTTP API (FastAPI or Flask).
- **Protocol:** B.L.A.S.T.
- **3-Layer Architecture:**
    - **Layer 1 (SOPs):** Prompts & Conversion Logic.
    - **Layer 2 (Nav):** API Routes & Orchestration.
    - **Layer 3 (Tools):** File I/O, LLM Client.

