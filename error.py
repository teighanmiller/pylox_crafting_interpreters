class Error:
    def __init__(self):
        self.had_error = False
    # Report errors
    def error(self, line: int, message: str):
        self._report(line, "", message)

    # Print errors
    def _report(self, line: int, where: str, message: str):
        print(f"[line {line}] Error{where}: {message}")
        self.had_error = True