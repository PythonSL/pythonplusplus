import random
import datetime
import os
import sys

class Runtime:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.last_output = None
        self.last_input = None

    def execute(self, line: str):
        parts = line.split()
        cmd = parts[0]

        if cmd == "print":
            text = " ".join(parts[1:])
            text = self._resolve(text)
            print(text)
            self.last_output = text

        elif cmd == "prompt" or cmd == "ask":
            text = " ".join(parts[1:])
            text = self._resolve(text)
            self.last_input = input(text + " ")
            self.variables["user_input"] = self.last_input

        elif cmd == "echo":
            text = " ".join(parts[1:])
            text = self._resolve(text)
            print(text, end="")
            self.last_output = text

        elif cmd == "set":
            if "=" in line:
                name, value = line.split("=", 1)
                name = name.replace("set", "").strip()
                value = self._resolve(value.strip())
                self.variables[name] = value

        elif cmd == "copy":
            if "=" in line:
                name, value = line.split("=", 1)
                name = name.replace("copy", "").strip()
                value = self._resolve(value.strip())
                self.variables[name] = value

        elif cmd == "clear":
            varname = parts[1]
            if varname in self.variables:
                del self.variables[varname]

        elif cmd == "add":
            a, _, b = parts[1:]
            a, b = self._resolve(a), self._resolve(b)
            result = str(int(a) + int(b))
            print(result)
            self.last_output = result

        elif cmd == "sub":
            a, _, b = parts[1:]
            a, b = self._resolve(a), self._resolve(b)
            result = str(int(a) - int(b))
            print(result)
            self.last_output = result

        elif cmd == "join":
            a, _, b = parts[1:]
            a, b = self._resolve(a), self._resolve(b)
            result = a + b
            print(result)
            self.last_output = result

        elif cmd == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(now)
            self.last_output = now

        elif cmd == "date":
            today = datetime.date.today().isoformat()
            print(today)
            self.last_output = today

        elif cmd == "random":
            if "to" in parts:
                start = int(self._resolve(parts[1]))
                end = int(self._resolve(parts[3]))
                result = str(random.randint(start, end))
                print(result)
                self.last_output = result

        elif cmd == "run":
            system_cmd = " ".join(parts[1:])
            os.system(system_cmd)

        elif cmd == "stop":
            sys.exit(0)

        else:
            if cmd in self.functions:
                self.execute(self.functions[cmd])
            else:
                print(f"Unknown command: {cmd}")

    def _resolve(self, value: str):
        if value in self.variables:
            return self.variables[value]
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        return value
