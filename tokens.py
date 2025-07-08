from typing import Final
from token_type import TokenType

class Token:
    #####
    type: Final[TokenType]
    lexeme: Final[str]
    literal: Final[object]
    line: Final[int]

    # Initilization of Token class and argument assignments
    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    # Defined print function for this class
    def __repr__(self):
        return self.type.name + " " + self.lexeme #+ " " + self.literal
    
    