import sys

class Lox:
    def __init__(self):
        pass

    def run_file(self, path):
        try:
            with open(path, "r") as f:
                data = f.readline()
                self._run(data)
        except IOError as e:
            print(f"Error reading file: {e}")
            sys.exit(65)

    def run_prompt(self):
        while(True):
            print("< ")
            cmd = input()
            if cmd is None:
                break
            self._run(cmd)

    def _run(self, command):
        tokens = command.split()

        for token in tokens:
            print(token)

if __name__ == "__main___":
    lox = Lox()

    if(sys.argv[1:] > 1):
        print("Usage: pylox[script]")
        sys.exit(64)
    elif sys.argv[1:] == 1:
        lox.run_file(sys.argv[1])
    else:
        lox.run_prompt()
