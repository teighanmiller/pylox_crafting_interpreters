import sys

class Lox:
    def __init__(self):
        had_error = False

    def run_file(self, path):
        try:
            # read the file passed in the argument
            with open(path, "r") as f:
                data = f.readline()
                self._run(data)
        # Error handling if file cannot be read.
        except IOError as e:
            print(f"Error reading file: {e}")
            sys.exit(65)

    def run_prompt(self):
        while(True):
            cmd = input("> ")
            if cmd is None:
                break
            self._run(cmd)
            self.had_error = False

    def _run(self, command):
        if self.had_error:
            sys.exit(65)
        tokens = command.split()
        for token in tokens:
            print(token)

    def error(self, line, message):
        self._report(line, "", message)

    def _report(self, line, where, message):
        print(f"[line {line}] Error{where}: {message}")
        self.had_error = True

if __name__ == "__main__":
    lox = Lox()

    # Check if the length of the command call.
    # If more than one argument is passed exit.
    if len(sys.argv[1:]) > 1:
        print("Usage: pylox [script]")
        sys.exit(64)
    # If one argument is passed run the file
    elif len(sys.argv[1:]) == 1:
        lox.run_file(sys.argv[0])
    # If no arguments are passed run the prompt
    else:
        lox.run_prompt()
