def run_pypp(code: str):
    lines = code.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Commands
        if line.startswith("say "):
            print(line[4:].strip())

        elif line.startswith("input:"):
            prompt = line[6:].strip()
            user_input = input(prompt + " ")
            print(f"You typed: {user_input}")

        elif line.startswith("repeat "):
            parts = line.split(maxsplit=2)
            if len(parts) >= 3:
                count = int(parts[1])
                text = parts[2]
                for _ in range(count):
                    print(text)
            else:
                print("Invalid repeat syntax. Use: repeat <count> <text>")

        else:
            print(f"Unknown command: {line}")
