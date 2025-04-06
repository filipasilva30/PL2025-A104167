class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.next_token()

    def check(self, token_type):
        if self.current_token[0] == token_type:
            self.lexer.advance()
            self.current_token = self.lexer.next_token()
        else:
            raise ValueError(f"Erro de sintaxe: Esperado {token_type}, mas encontrou {self.current_token[0]}")

    def factor(self):
        """Factor → NUM | ‘(’ Expr ‘)’"""
        token = self.current_token
        if token[0] == 'NUM':
            self.check('NUM')
            return int(token[1])
        elif token[0] == 'LPAREN':
            self.check('LPAREN')
            result = self.expr()
            self.check('RPAREN')
            return result
        else:
            raise ValueError("Erro de sintaxe: Fator inválido")

    def term(self):
        """Term → Factor ((‘*’ | ‘/’) Factor)*"""
        result = self.factor()
        while self.current_token[0] in ('MULT', 'DIV'):
            if self.current_token[0] == 'MULT':
                self.check('MULT')
                result *= self.factor()
            elif self.current_token[0] == 'DIV':
                self.check('DIV')
                result //= self.factor()  # Inteiro para simplificação
        return result

    def expr(self):
        """Expr → Term ((‘+’ | ‘-’) Term)*"""
        result = self.term()
        while self.current_token[0] in ('ADI', 'SUB'):
            if self.current_token[0] == 'ADI':
                self.check('ADI')
                result += self.term()
            elif self.current_token[0] == 'SUB':
                self.check('SUB')
                result -= self.term()
        return result

    def parse(self):
        return self.expr()
