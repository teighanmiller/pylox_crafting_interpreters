from error import Error
from token_type import TokenType
from tokens import Token

class Scanner:
    def __init__(self, source: str):
        # storage for original passed string
        self._source = source
        # storage for individual tokens
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 1

    def scan_tokens(self):
        while(not self._isAtEnd()):
            # We are at the beginning of the next lexeme
            self._start = self._current
            self._scanToken()
        
        # Create new token for the end of the file
        new_token = Token(TokenType.EOF, "", None, self._line)
        # Add end of file token to the end of tokens list
        self._tokens.append(new_token)
        return self._tokens

    def _isAtEnd(self):
        # Check if location is at the end of the source string
        return self._current >= len(self._source)

    def _scanToken(self):
        c = self._advance()

        # Recognize lexemes
        # Single character lexemes
        if c == '(':
            self._add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self._add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self._add_token(TokenType.RIGHT_BRACE)
        elif c == '}':
            self._add_token(TokenType.LEFT_BRACE)
        elif c == ',':
            self._add_token(TokenType.COMMA)
        elif c == '.':
            self._add_token(TokenType.DOT)
        elif c == '-':
            self._add_token(TokenType.MINUS)
        elif c == '+':
            self._add_token(TokenType.PLUS)
        elif c == ';':
            self._add_token(TokenType.SEMICOLON)
        elif c == '*':
            self._add_token(TokenType.STAR)
        elif c == '!':
        # Double character lexemes
            self._add_token(TokenType.BANG_EQUAL if self._match('=') else TokenType.BANG)
        elif c == '=':
            self._add_token(TokenType.EQAUL_EQAUL if self._match('=') else TokenType.EQAUL)
        elif c == '<':
            self._add_token(TokenType.LESS_EQAUL if self._match('=') else TokenType.LESS)
        elif c == '>':
            self._add_token(TokenType.GREATER_EQAUL if self._match('=') else TokenType.GREATER)
        # Special handling for '/' because comments and division begin with '/'
        elif c == '/':
            # If the next character after the '/' is '/' then comment
            if self._match('/'):
                # Consume characters until end of line because everything after '//' is a comment
                while self._peek() != '\n' and not self._isAtEnd():
                    self._advance()
            # Otherwise it is a slash token and a division symbol
            else:
                self._add_token(TokenType.SLASH)
        # Ignore special characters
        elif c == ' ':
            pass
        elif c == '\r':
            pass
        elif c == '\t':
            pass
        # Move to newline on line break
        elif c == '\n':
            self._line += 1
        # Create a string
        elif c == '"':
            self._string()
        else:
            if self._isDigit(c):
                self._number()
            # Matching for reserved words
            elif self._isAlpha(c):
                self._identifier()
        # Handle unsupported characters
            else:
                Error.error(self._line, "Unexpected character.")

    def _identifier(self):
        # Check if next character is alpha numeric and advance
        while(self._isAlphaNumeric(self._peek())):
            self._advance()
        # Get the full word
        text = self._source[self._start:self._current]

        # Check if word is a keyword
        typ = self._keywords.get(text)

        # If not keyword create a user defined identifier
        if typ == None:
            typ = TokenType.INDENTIFIER
        self._add_token(typ)

    def _number(self):
        # Consume characters while characters are digits
        while self._isDigit(self._peek()):
            self._advance()

        # Check for . indicating decimal number and continue till end of number
        # Checks for digits after decimal before consuming character
        if self._peek() == '.' and self._isDigit(self._peekNext()):
            self._advance()

            while self._isDigit(self._peek()):
                self._advance()

        # Create the token for the number
        self._addToken(TokenType.NUMBER, float(self._source[self._start:self._current]))

    def _string(self):
        # Consume characters until end of string or end of file.
        while self._peek() != '"' and not self._isAtEnd():
            # Move to next line
            if self._peek() == '\n':
                self._line += 1
            
            # Move forward a character
            self._advance()
        
        # If we find the end of the file without string terminator raise error.
        if self._isAtEnd():
            Error.error(self._line, "Unterminated string.")
            return

        # The closing ".
        self._advance()

        # Trim the surrounding quotes
        value = self._source[self._start + 1: self._current - 1]
        self._addToken(TokenType.STRING, value)

    # Consumes character only if it is what we are looking for
    # Used for two character lexemes
    def _match(self, expected: str):
        # Check if EOF
        if self._isAtEnd():
            return False
        
        # Check if the current token is the expected one
        if self._source[self._current] != expected:
            return False

        # Move to the next character in the source file
        self._current += 1
        return True

    # Looks ahead without consuming a character
    def _peek(self):
        if self._isAtEnd():
            return '\0'
        return self._source[self._current]

    # Look ahead for second character
    def _peekNext(self):
        if self._current + 1 >= len(self._source) - 1:
            return '\0'
        return self._source[self._current + 1]

    # Check if character is letter or number
    def _isAlphaNumeric(self, c):
        return self._isAlpha(c) or self._isDigit(c)
    
    # Check if lower, uppercase letters or "_" character
    def _isAlpha(self, c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c == '_')

    # Check if digit
    def _isDigit(self, c: str) -> bool:
       return c >= '0' and c <= '9'
    
    def _advance(self):
        # Consume the next token in the source file and return
        c = self._source[self._current]
        self._current += 1
        return c 

    def _add_token(self, type: TokenType):
        # Create a new token for current lexeme
        self._addToken(type, None)

    def _addToken(self, type: TokenType, literal: object):
        # Overload used to handle literal values
        text = self._source[self._start:self._current]
        self._tokens.append(Token(type, text, literal, self._line))

    # Dictionary of keywords
    _keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE
    }
        
