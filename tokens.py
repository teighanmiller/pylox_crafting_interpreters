import Lox
from typing import Final
from TokenType import TokenType

class Token:
    type: Final[TokenType]
    
    