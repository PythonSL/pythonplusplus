import os
import shutil
import stat

HOME = os.path.expanduser("~")
INSTALL_DIR = os.path.join(HOME, ".local", "share", "pypp")
BIN_DIR = os.path.join(HOME, ".local", "bin")
BIN_PATH = os.path.join(BIN_DIR, "pypp")

def main():
    print("[*] Installing Py++...")

    # 1. copy source files
    if os.path.exists(INSTALL_DIR):
        shutil.rmtree(INSTALL_DIR)
    shutil.copytree("pypp", INSTALL_DIR)
    print(f"[+] Installed core files to {INSTALL_DIR}")

    # 2. make bin dir if missing
    os.makedirs(BIN_DIR, exist_ok=True)

    # 3. create wrapper script
    wrapper = f"""#!/usr/bin/env bash
python3 {INSTALL_DIR}/cli.py "$@"
"""
    with open(BIN_PATH, "w") as f:
        f.write(wrapper)

    # 4. make executable
    st = os.stat(BIN_PATH)
    os.chmod(BIN_PATH, st.st_mode | stat.S_IEXEC)
    print(f"[+] Created launcher at {BIN_PATH}")

    print("\n[*] Done! Make sure ~/.local/bin is in your PATH.")
    print("    Then you can run: pypp run tests/hello.pypp")

if __name__ == "__main__":
    main()
