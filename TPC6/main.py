from lexer import Lexer
from parser import Parser

def main():
    while True:
        try:
            text = input(">> ")
            if text.lower() in ('exit', 'quit'):
                print("Encerrar...")
                break

            lexer = Lexer(text)
            parser = Parser(lexer)
            result = parser.parse()
            print(f"Resultado: {result}")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()