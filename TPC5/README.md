# TPC5 (14/03/2025)
- Nome: Filipa Oliveira da Silva
- Número: A104167

![Foto](https://avatars.githubusercontent.com/u/144493282?v=4)

## Resumo
Este trabalho consiste no desenvolvimento de um programa que simula uma ***máquina de vending***. O sistema permite que o utilizador
interaja com a máquina, inserindo moedas, listando os produtos disponíveis e selecionando os produtos que deseja, recebendo o respetivo
troco, caso seja necessário. O stock de produtos é armazenado num arquivo JSON, chamado **stock.json**.

## Funcionalidades
- **Listagem de Produtos:** exibe todos os produtos disponíveis na máquina, com informações sobre o código, nome, quantidade
e preço de cada um.
- **Inserção de Moedas:** o utilizador insere moedas(euros ou cêntimos), aumentando o saldo disponível para compra.
- **Seleção de Produtos:** comando que permite ao utilizador selecionar um produto com base no código fornecido. A compra apenas é
realizada caso o saldo seja suficiente e o produto esteja disponível.
- **Troco:** aquando da utilização do comando ***SAIR***, a máquina exibe o troco, se houver, baseado nas moedas inseridas e no saldo 
final.
- **Saída:** quando o utilizador digita ***SAIR***, o programa termina e exibe a mensagem final.  

## Implementação
O script foi implementado em Python utilizando as bibliotecas ***re*** para expressões regulares e ***json*** para o armazenamento e leitura 
do stock de produtos. A máquina é capaz de processar comandos de interação, mantendo o controlo do saldo e do stock durante a execução.

## Lista de Resultados
- [`vending.py`](./vending.py)

### Exemplo
- **Input**
```
LISTAR
MOEDA 1e, 50c .
SELECIONAR B15
SAIR
```

- **Output**
```
maq:
cod | nome | quantidade | preço
----------------------------------------
A23 água 0.5L 7 0.7€
B15 sumo laranja 4 1.2€
C30 batatas fritas 10 1.0€

maq: Saldo = 1e50c

maq: Pode retirar o produto dispensado "sumo laranja"
maq: Saldo = 0e30c

Pode retirar o troco: 1x 20c, 1x 10c
maq: Até à próxima!
```