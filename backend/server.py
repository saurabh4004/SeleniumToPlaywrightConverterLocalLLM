from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Add parent directory to path to import tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.llm_client import query_ollama
from tools.file_ops import save_code_to_file

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConversionRequest(BaseModel):
    source_code: str
    output_filename: str
    target_language: str = "typescript"

class ConversionResponse(BaseModel):
    success: bool
    converted_code: str
    file_path: str
    message: str

def load_system_prompt():
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "architecture", "prompt_sop.md")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading prompt SOP: {e}")
        return "You are an expert code converter."

SYSTEM_PROMPT = load_system_prompt()

@app.post("/convert", response_model=ConversionResponse)
async def convert_code(request: ConversionRequest):
    try:
        # Construct the full prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nHere is the Java code to convert:\n\n```java\n{request.source_code}\n```"
        
        # Call Ollama
        print(f"Sending request to Ollama for {request.output_filename}...")
        converted_code = query_ollama(full_prompt, model="codellama")
        
        # Clean up the output
        # 1. Remove markdown code blocks
        clean_code = converted_code.replace("```typescript", "").replace("```", "").strip()
        
        # 2. Heuristic: If output contains "import", assume code starts there.
        if "import" in clean_code:
            clean_code = clean_code[clean_code.find("import"):]
            
        # 3. Heuristic: Strip any trailing notes after the last closing brace (risky if usage varies, but safe for standard tests)
        # Better: Just strip known conversational headers if step 2 didn't catch them.
        
        # Save to file
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
        file_path = save_code_to_file(clean_code, output_dir, request.output_filename)
        
        return ConversionResponse(
            success=True,
            converted_code=clean_code,
            file_path=file_path,
            message="Conversion successful"
        )
        
    except Exception as e:
        return ConversionResponse(
            success=False,
            converted_code="",
            file_path="",
            message=f"Error during conversion: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
