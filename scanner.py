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

    def _scanToken(self):
        c = self._advance()

        if c == '(':
            self._addToken(TokenType.LEFT_PAREN)
        elif c == ')':
            self._addToken(TokenType.RIGHT_PAREN)
        elif c == '{':
            self._addToken(TokenType.RIGHT_BRACE)
        elif c == '}':
            self._addToken(TokenType.LEFT_BRACE)
        elif c == ',':
            self._addToken(TokenType.COMMA)
        elif c == '.':
            self._addToken(TokenType.DOT)
        elif c == '-':
            self._addToken(TokenType.MINUS)
        elif c == '+':
            self._addToken(TokenType.PLUS)
        elif c == ';':
            self._addToken(TokenType.SEMICOLON)
        elif c == '*':
            self._addToken(TokenType.STAR)
        elif c == '!':
            self._addToken(TokenType.BANG_EQUAL if self._match('=') else TokenType.BANG)
        elif c == '=':
            self._addToken(TokenType.EQAUL_EQAUL if self._match('=') else TokenType.EQAUL)
        elif c == '<':
            self._addToken(TokenType.LESS_EQAUL if self._match('=') else TokenType.LESS)
        elif c == '>':
            self._addToken(TokenType.GREATER_EQAUL if self._match('=') else TokenType.GREATER)
        elif c == '/':
            if self._match('/'):
                while self._peek() != '\n' and not self._isAtEnd():
                    self._advance()
            else:
                self._addToken(TokenType.SLASH)
        elif c == ' ':
            pass
        elif c == '\r':
            pass
        elif c == '\t':
            pass
        elif c == '\n':
            self._line += 1
        else:
            Lox.error(self._line, "Unexpected character.")

    def _match(self, expected: str):
        if self._isAtEnd():
            return False
        
        if self._source[self._current] != expected:
            return False

        self._current += 1
        return True

    def _peek(self):
        if self._isAtEnd():
            return '\0'
        return self._source[self._current]
    
    def _advance(self):
        return self._source[self._current + 1]

    def _addToken(self, type: TokenType):
        self._addToken(type, None)

    def _addToken(self, type: TokenType, literal: object):
        text = self._source[self._start:self._current]
        self._tokens.append(Token(type, text, literal, self._line))
        
