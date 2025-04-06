# TPC6 (06/04/2025)
- Nome: Filipa Oliveira da Silva
- Número: A104167

![Foto](https://avatars.githubusercontent.com/u/144493282?v=4)

## Resumo
Este trabalho consiste no desenvolvimento de um parser LL(1), ou seja, um **parser recursivo descendente** que reconhece expressões aritméticas
e calcula o seu respetivo valor. O programa é composto por três ficheiros principais: um **analisador léxico** (lexer.py), um **analisador sintático** 
(parser.py) e um **ficheiro de entrada principal** (main.py).

## Implementação
- **lexer.py:** responsável por identificar e separar os diferentes tokens da expressão e usa expressões regulares para construir uma lista de tokens 
a partir do texto de entrada.
- **parser.py:** contém a implementação do parser LL(1), com base numa gramática que respeita a precedência dos operadores. Para isso, define os métodos
*expr*, *term* e *factor*, que analisam e avaliam a expressão de forma recursiva.
- **main.py:** interação com o utilizador, recebendo expressões como input, invocando o lexer e parser e apresentando o resultado calculado.

## Lista de Resultados
- [`lexer.py`](./lexer.py)
- [`parser.py`](./parser.py)
- [`main.py`](./main.py)

### Exemplo
- **Input**
```
2+3
```
```
67-(2+3*4)
```
```
(9-2)*(13-4)
```

- **Output**
```
Resultado: 5
```
```
Resultado: 53
```
```
Resultado: 63
```