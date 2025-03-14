import re
import json

# Carregar stock do JSON
def carregar_stock():
    with open("stock.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Guardar stock no JSON
def guardar_stock(stock):
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

# Moedas para troco (em cêntimos)
MOEDAS_TROCO = [100, 50, 20, 10, 5, 2, 1]

TOKEN_REGEX = {
    "LISTAR": r"^LISTAR$",
    "MOEDA": r"^MOEDA\s+(\d+[ec](?:,\s*\d+[ec])*)\s*\.\s*$",
    "SELECIONAR": r"^SELECIONAR\s+[A-Z]\d{2}$",
    "SAIR": r"^SAIR$"
}

# Interpretador dos comandos
def interpretar(comando, stock, saldo):
    for token, pattern in TOKEN_REGEX.items():
        if re.match(pattern, comando):
            if token == "LISTAR":
                print("maq:\ncod | nome | quantidade | preço")
                print("-" * 40)
                for item in stock:
                    print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}€")
                return saldo
            elif token == "MOEDA":
                match = re.match(TOKEN_REGEX["MOEDA"], comando)
                if match:
                    moedas = match.group(1).split(",")  # Obtém a parte das moedas e divide por vírgula
                    for moeda in moedas:
                        moeda = moeda.strip()  # Remove espaços em excesso
                        valor, tipo = int(moeda[:-1]), moeda[-1]  # Separa o valor do tipo (e ou c)
                        if tipo == "e":
                            saldo += valor * 100  # Converter euros para cêntimos
                        elif tipo == "c":
                            saldo += valor  
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
                return saldo

            elif token == "SELECIONAR":
                cod_prod = comando.split()[1]
                produto = next((p for p in stock if p["cod"] == cod_prod), None)

                if not produto:
                    print("maq: Produto inexistente")
                    return saldo

                if produto["quant"] == 0:
                    print(f"maq: Produto {produto['nome']} esgotado")
                    return saldo

                preco_produto = int(produto["preco"] * 100)  # Preço em cêntimos

                if saldo < preco_produto:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {preco_produto // 100}e{preco_produto % 100}c")
                    return saldo

                produto["quant"] -= 1
                saldo -= preco_produto
                print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
                print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
                return saldo

            elif token == "SAIR":
                # Calcular o troco
                troco = saldo
                moedas_troco = {}
                for moeda in MOEDAS_TROCO:
                    quantidade = troco // moeda
                    if quantidade > 0:
                        moedas_troco[moeda] = quantidade
                    troco = troco % moeda

                troco_str = ", ".join([f"{quant}x {moeda // 100 if moeda >= 100 else moeda}c" 
                                       for moeda, quant in moedas_troco.items()])
                print(f'Pode retirar o troco: {troco_str}')
                print("maq: Até à próxima!")
                return saldo

    print("maq: Comando inválido!")
    return saldo

def main():
    stock = carregar_stock()
    saldo = 0
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip()
        saldo = interpretar(comando, stock, saldo)
        if comando == "SAIR":
            guardar_stock(stock)
            break

if __name__ == "__main__":
    main()