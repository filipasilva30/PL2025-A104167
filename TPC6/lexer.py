import re

# Tipos de tokens
TOKEN_REGEX = [
    (r'\d+', 'NUM'),       # Números inteiros
    (r'\+', 'ADI'),        # +
    (r'-', 'SUB'),         # -
    (r'\*', 'MULT'),       # *
    (r'/', 'DIV'),         # /
    (r'\(', 'LPAREN'),     # (
    (r'\)', 'RPAREN')      # )
]

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = self.tokenize(input_text)
        self.pos = 0

    def tokenize(self, text):
        tokens = []
        while text:
            text = text.strip()                             # Remove espaços à esquerda
            for pattern, token_type in TOKEN_REGEX:
                match = re.match(pattern, text)
                if match:
                    tokens.append((token_type, match.group()))
                    text = text[len(match.group()):]
                    break
            else:
                raise ValueError(f"Caractere inválido: {text[0]}")
        tokens.append(("EOF", ""))  # Fim da entrada
        return tokens

    def next_token(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1