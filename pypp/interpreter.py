from pypp.runtime import Runtime

class Interpreter:
    def __init__(self):
        self.runtime = Runtime()

    def run(self, tokens):
        for line in tokens:
            self.runtime.execute(line)
