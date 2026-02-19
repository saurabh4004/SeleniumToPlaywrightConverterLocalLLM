import requests
import json

URL = "http://localhost:11434/api/generate"

def test_model(model_name: str):
    print(f"Testing model: {model_name}...")
    try:
        resp = requests.post(URL, json={
            "model": model_name,
            "prompt": "Say hi.",
            "stream": False
        }, timeout=30)
        print(f"Result ({model_name}): {resp.status_code} - {resp.json().get('response')[:20]}")
    except Exception as e:
        print(f"Error ({model_name}): {e}")

if __name__ == "__main__":
    test_model("codellama:latest")
    # test_model("codellama:latest") # Uncomment if you want to test codellama next
