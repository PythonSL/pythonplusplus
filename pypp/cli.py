import sys
from interpreter import run_pypp

def main():
    if len(sys.argv) < 2:
        print("Usage: pypp <file.pypp>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    print(f"Running Py++ file: {file_path}")
    run_pypp(code)

if __name__ == "__main__":
    main()
