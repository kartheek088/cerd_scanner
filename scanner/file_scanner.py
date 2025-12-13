import os

IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__'}

def scan_files(root_path):
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, start=1):
                        yield file_path, i, line.strip()
            except Exception:
                continue
