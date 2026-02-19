import requests
import json
import os

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt: str, model: str = "codellama") -> str:
    """
    Sends a prompt to the local Ollama instance and returns the generated code.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Increase timeout to 180 seconds for slow local models
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.Timeout:
        print("Error: Ollama request timed out ( > 180s). Model might be loading or too slow.")
        return "Error: Request timed out. The local model is taking too long to respond."
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Test the connection
    print("Testing Ollama Connection...")
    result = query_ollama("Write a specialized 'Hello World' in TypeScript.", model="codellama")
    print(f"Response:\n{result}")
