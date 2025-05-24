import Lox
from typing import Final
from token_type import TokenType

class Token:
    type: Final[TokenType]

    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def to_string(self):
        return self.type + " " + self.lexeme + " " + self.literal
    
    