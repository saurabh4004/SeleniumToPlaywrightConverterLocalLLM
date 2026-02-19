# Task Plan

## Phases
## Phases

### Phase 1: Blueprint (Discovery & Logic) - [IN PROGRESS]
- [x] Define Vision & North Star.
- [x] Define Data Schemas.
- [ ] Research/Verify Ollama connection.
- [ ] Create Prompt Strategy (SOP) for Java -> TS conversion.

### Phase 2: Link (Connectivity)
- [ ] **Check 1:** Verify Ollama is running and accessible (local API).
- [ ] **Check 2:** Verify Python environment (install `requests`, `fastapi`, `uvicorn`).
- [ ] Create `tools/llm_client.py` to handle communication with Ollama.
- [ ] "Hello World" test: Send a simple string to Ollama and get a response.

### Phase 3: Architect (The Engine)
- [ ] Create `tools/file_ops.py` (Save to directory).
- [ ] Create `architecture/prompt_sop.md` (Define the system prompt for the LLM).
- [ ] Build `backend/server.py` (FastAPI app).
    - [ ] `/convert` endpoint implementation.

### Phase 4: Stylize (The UI)
- [ ] Create `frontend/index.html` (Layout & Structure).
- [ ] Create `frontend/style.css` (Rich Aesthetics, Dark Mode, Glassmorphism).
- [ ] Create `frontend/app.js` (Logic: Fetch API -> Backend -> Display).

### Phase 5: Trigger (Deployment/Run)
- [ ] Final End-to-End Test.
- [ ] Write `README.md` with usage instructions.


## Current Goals
- Initialize project memory files.
- Complete Discovery phase.
