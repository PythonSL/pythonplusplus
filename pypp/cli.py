import sys
import os

def run_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        # Run the code as if it was Python
        exec(code, globals())
    except Exception as e:
        print(f"Error while running {filename}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: pypp <file.pypp>")
        return

    filename = sys.argv[1]
    run_file(filename)

if __name__ == "__main__":
    main()
