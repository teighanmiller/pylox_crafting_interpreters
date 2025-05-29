import Lox
from token_type import TokenType
from tokens import Token

class Scanner:
    _source: str
    _tokens = []
    _start = 0
    _current = 0
    _line = 1

    def __init__(self, source: str):
        self._source = source

    def scan_tokens(self):
        while(not self._isAtEnd):
            # We are at the beginning of the next lexeme
            self._start = self._current
            self.scan_token()
        
        new_token = Token(TokenType.EOF, "", None, self._line)
        self._tokens.add(new_token)
        return self._tokens

    def scan_token(self):
        c = self.advance()

    def _isAtEnd(self):
        return self._current >= len(self._source)
        
