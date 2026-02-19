import shutil
import os

def create_zip():
    base_name = "Selenium2PlaywrightConverter"
    root_dir = os.getcwd()
    format = "zip"
    
    # Files to ignore (exclude based on .gitignore essentially)
    def ignore_patterns(dir, files):
        ignores = ["__pycache__", ".git", ".env", ".tmp", "output", "temp_files"]
        return [f for f in files if f in ignores or f.endswith(".pyc")]

    try:
        shutil.make_archive(base_name, format, root_dir)
        print(f"Created {base_name}.zip")
    except Exception as e:
        print(f"Error creating zip: {e}")

if __name__ == "__main__":
    create_zip()
