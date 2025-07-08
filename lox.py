import sys
from error import Error
from scanner import Scanner

class Lox:
    def __init__(self):
        # Boolean for errors
        self.error_handler = Error()

    def run_file(self, path: str):
        try:
            # read the file passed in the argument
            with open(path, "r") as f:
                data = f.readline()
                self._run(data)
                if self.error_handler.had_error:
                    # Indicate an error in the exit code
                    raise IOError
        # Error handling if file cannot be read.
        except IOError as e:
            print(f"Error reading file: {e}")
            sys.exit(65)

    def run_prompt(self):
        # Put out shell syntax when Lox.py is called
        while(True):
            # Wait for command
            cmd = input("> ")

            # Exit command prompt if "exit" is typed
            if cmd == "exit":
                break
            # Run command
            self._run(cmd)
            # Reset error boolean
            self.error_handler.had_error = False

    # Run command given
    def _run(self, command: str):
        # Scan the line
        scanner = Scanner(command)
        # Split the tokens
        tokens = scanner.scan_tokens()
        # Print the tokens
        for token in tokens:
            print(token)

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
