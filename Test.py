import os
import sys

file = sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Main')))

def process_line(line, file_path, line_number):
    """
    Customize this function to process each line.
    Example: print lines containing 'TODO'
    """
    if 'TODO' in line:
        print(f"TODO found in {file_path} at line {line_number}: {line.strip()}")

def scan_python_files(folder_path):
    """Scan all Python files in the given folder and process each line."""
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line_number, line in enumerate(f, start=1):
                            process_line(line, file_path, line_number)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

# Example usage:
scan_python_files("C:\Users\giopr\Desktop\GOA-PROJECT\Main")
