import os
import random
import time

def run_pypp(code: str):
    lines = code.splitlines()
    variables = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # SAY
        if line.startswith("say "):
            print(line[4:].strip())

        # INPUT
        elif line.startswith("input:"):
            prompt = line[6:].strip()
            user_input = input(prompt + " ")
            print(f"You typed: {user_input}")

        # REPEAT
        elif line.startswith("repeat "):
            parts = line.split(maxsplit=2)
            if len(parts) >= 3:
                count = int(parts[1])
                text = parts[2]
                for _ in range(count):
                    print(text)
            else:
                print("Invalid repeat syntax. Use: repeat <count> <text>")

        # CLEAR SCREEN
        elif line == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        # WAIT
        elif line.startswith("wait "):
            try:
                seconds = float(line.split()[1])
                time.sleep(seconds)
            except:
                print("Invalid wait command")

        # RANDOM NUMBER
        elif line.startswith("rand "):
            parts = line.split()
            if len(parts) == 3:
                low, high = int(parts[1]), int(parts[2])
                print(random.randint(low, high))
            else:
                print("Usage: rand <min> <max>")

        # STORE VARIABLE
        elif line.startswith("set "):
            try:
                _, name, value = line.split(maxsplit=2)
                variables[name] = value
            except:
                print("Usage: set <name> <value>")

        # PRINT VARIABLE
        elif line.startswith("get "):
            name = line.split()[1]
            print(variables.get(name, f"{name} not defined"))

        # SIMPLE IF
        elif line.startswith("if "):
            try:
                _, name, value, _, command = line.split(maxsplit=4)
                if variables.get(name) == value:
                    run_pypp(command)
            except:
                print("Usage: if <var> <value> then <command>")

        # EXIT
        elif line == "exit":
            print("Exiting Py++...")
            break

        # 40+ FUN SIMPLE COMMANDS
        elif line == "hello":
            print("Hello from Py++!")

        elif line == "time":
            print("Current time:", time.strftime("%H:%M:%S"))

        elif line == "date":
            print("Today is:", time.strftime("%Y-%m-%d"))

        elif line == "joke":
            print("Why do programmers hate nature? Too many bugs.")

        elif line == "coin":
            print(random.choice(["Heads", "Tails"]))

        elif line == "dice":
            print("You rolled:", random.randint(1, 6))

        elif line == "yesno":
            print(random.choice(["Yes", "No"]))

        elif line.startswith("echo "):
            print(line[5:])

        elif line == "whoami":
            print(os.getlogin())

        elif line == "cwd":
            print(os.getcwd())

        elif line.startswith("cd "):
            try:
                os.chdir(line[3:].strip())
                print("Changed directory to", os.getcwd())
            except Exception as e:
                print("Error:", e)

        elif line == "list":
            print("\n".join(os.listdir()))

        elif line.startswith("math add "):
            a, b = map(int, line.split()[2:])
            print(a + b)

        elif line.startswith("math sub "):
            a, b = map(int, line.split()[2:])
            print(a - b)

        elif line.startswith("math mul "):
            a, b = map(int, line.split()[2:])
            print(a * b)

        elif line.startswith("math div "):
            a, b = map(int, line.split()[2:])
            print(a / b)

        elif line == "about":
            print("Py++ Test Language v1.0")

        elif line == "version":
            print("Py++ version 1.0.0")

        elif line == "help":
            print("Available commands: say, input, repeat, clear, wait, rand, set, get, if, exit, hello, time, date, joke, coin, dice, yesno, echo, whoami, cwd, cd, list, math add/sub/mul/div, about, version, help")

        else:
            print(f"Unknown command: {line}")
