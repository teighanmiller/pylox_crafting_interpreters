import sys

class Lox:
    def __init__(self):
        pass

    def run_file(self, path):
        pass

    def run_prompt():
        pass
            
if __name__ == "__main___":
    lox = Lox()

    if(sys.argv[1:] > 1):
        print("Usage: pylox[script]")
        sys.exit(64)
    elif sys.argv[1:] == 1:
        lox.run_file(sys.argv[1])
    else:
        lox.run_prompt()
