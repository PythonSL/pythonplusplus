import random
import time
import datetime
import os
import sys

variables = {}

def parse_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        i = parse_line(lines, i)

def parse_line(lines, i):
    line = lines[i].strip()
    if not line or line.startswith("#"):
        return i + 1

    parts = line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    # ---------------- BASIC OUTPUT ----------------
    if cmd in ["print", "say", "echo"]:
        print(" ".join(args).replace('"', ''))
    elif cmd == "shout":
        print(" ".join(args).replace('"', '').upper())
    elif cmd == "whisper":
        print(" ".join(args).replace('"', '').lower())
    elif cmd == "newline":
        print()

    # ---------------- INPUT ----------------
    elif cmd == "ask":
        inp = input(" ".join(args).replace('"', '') + " ")
        variables["_last"] = inp
    elif cmd == "asknum":
        inp = input(" ".join(args).replace('"', '') + " ")
        try:
            variables["_last"] = int(inp)
        except:
            variables["_last"] = 0

    # ---------------- VARIABLES ----------------
    elif cmd == "let":
        name = args[0]
        value = " ".join(args[2:]).replace('"', '')
        try:
            variables[name] = int(value)
        except:
            variables[name] = value
    elif cmd == "show":
        name = args[0]
        print(variables.get(name, "undefined"))

    # ---------------- MATH ----------------
    elif cmd == "add":
        print(int(variables.get(args[0], args[0])) + int(variables.get(args[1], args[1])))
    elif cmd == "sub":
        print(int(variables.get(args[0], args[0])) - int(variables.get(args[1], args[1])))
    elif cmd == "mul":
        print(int(variables.get(args[0], args[0])) * int(variables.get(args[1], args[1])))
    elif cmd == "div":
        print(int(variables.get(args[0], args[0])) / int(variables.get(args[1], args[1])))
    elif cmd == "mod":
        print(int(variables.get(args[0], args[0])) % int(variables.get(args[1], args[1])))
    elif cmd == "pow":
        print(int(variables.get(args[0], args[0])) ** int(variables.get(args[1], args[1])))
    elif cmd == "rand":
        print(random.randint(int(args[0]), int(args[1])))

    # ---------------- SYSTEM ----------------
    elif cmd == "time":
        print(datetime.datetime.now().strftime("%H:%M:%S"))
    elif cmd == "date":
        print(datetime.datetime.now().strftime("%Y-%m-%d"))
    elif cmd == "day":
        print(datetime.datetime.now().strftime("%A"))
    elif cmd == "wait":
        time.sleep(int(args[0]))
    elif cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif cmd == "exit":
        sys.exit(0)

    # ---------------- STRINGS ----------------
    elif cmd == "len":
        print(len(" ".join(args).replace('"', '')))
    elif cmd == "upper":
        print(" ".join(args).replace('"', '').upper())
    elif cmd == "lower":
        print(" ".join(args).replace('"', '').lower())
    elif cmd == "reverse":
        print(" ".join(args).replace('"', '')[::-1])
    elif cmd == "concat":
        print("".join(arg.replace('"', '') for arg in args))

    # ---------------- LISTS ----------------
    elif cmd == "list":
        variables["_lastlist"] = args
        print(args)
    elif cmd == "append":
        variables[args[0]].append(args[1])
    elif cmd == "remove":
        variables[args[0]].remove(args[1])
    elif cmd == "showlist":
        print(variables.get(args[0], []))
    elif cmd == "lenlist":
        print(len(variables.get(args[0], [])))
    elif cmd == "first":
        print(variables.get(args[0], [])[0])
    elif cmd == "last":
        print(variables.get(args[0], [])[-1])
    elif cmd == "range":
        print(list(range(int(args[0]), int(args[1]))))

    # ---------------- BOOL ----------------
    elif cmd == "and":
        print(bool(args[0]) and bool(args[1]))
    elif cmd == "or":
        print(bool(args[0]) or bool(args[1]))
    elif cmd == "not":
        print(not bool(args[0]))
    elif cmd == "true":
        print(True)
    elif cmd == "false":
        print(False)
    elif cmd == "typeof":
        print(type(variables.get(args[0], args[0])).__name__)

    # ---------------- COMMENTS ----------------
    elif cmd == "comment":
        pass

    else:
        print(f"Unknown command: {cmd}")

    return i + 1
