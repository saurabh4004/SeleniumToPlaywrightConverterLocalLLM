import os

def save_code_to_file(code: str, output_dir: str, filename: str) -> str:
    """
    Saves the provided code to a specific file.
    Returns the absolute path of the saved file.
    """
    try:
        # Ensure directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
            
        print(f"Successfully saved to {file_path}")
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return ""

if __name__ == "__main__":
    # Test
    save_code_to_file("// test content", "d:\\temp", "test.ts")
