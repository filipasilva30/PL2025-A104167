def ler_csv(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        conteudo = f.read()  # lê o ficheiro inteiro

    linhas = []
    linha_atual = ""
    dentro_aspas = False

    for caractere in conteudo:
        if caractere == '"':
            dentro_aspas = not dentro_aspas  
        
        if caractere == "\n" and not dentro_aspas:
            linhas.append(linha_atual)
            linha_atual = ""         # limpa para ler a próxima linha
        else:
            linha_atual += caractere

    # última linha, se houver
    if linha_atual:  
        linhas.append(linha_atual)

    cabecalho = linhas[0].strip().split(";")
    dados = []

    for linha in linhas[1:]:
        partes = []
        dentro_aspas = False
        campo_atual = ""

        for caractere in linha:
            if caractere == '"':
                dentro_aspas = not dentro_aspas
            elif caractere == ";" and not dentro_aspas:
                partes.append(campo_atual.strip())
                campo_atual = ""
            else:
                campo_atual += caractere

        partes.append(campo_atual.strip())          # último campo
        if len(partes) == len(cabecalho):  
            dados.append(dict(zip(cabecalho, partes)))

    return dados



def processar_dados(dados):
    # Lista de compositores ordenada
    compositores = sorted(set(obra['compositor'] for obra in dados))
    
    # Contagem de obras por período
    contagem_por_periodo = {}
    obras_por_periodo = {}
    
    for obra in dados:
        periodo = obra['periodo']
        nome_obra = obra['nome']
        
        contagem_por_periodo[periodo] = contagem_por_periodo.get(periodo, 0) + 1
        
        if periodo not in obras_por_periodo:
            obras_por_periodo[periodo] = []
        
        obras_por_periodo[periodo].append(nome_obra)
    
    # Dicionário das obras por período
    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()
    
    return compositores, contagem_por_periodo, obras_por_periodo


def main():
    nome_ficheiro = "obras.csv"
    dados = ler_csv(nome_ficheiro)
    compositores, contagem, obras_por_periodo = processar_dados(dados)
    
    print("Lista de Compositores:")
    print("\n".join(compositores))
    
    print("\nDistribuição das Obras por Período:")
    for periodo, quantidade in contagem.items():
        print(f"{periodo}: {quantidade} obras")
    
    print("\nDicionário de Obras por Período:")
    for periodo, obras in obras_por_periodo.items():
        print(f"{periodo}: {obras}")


if __name__ == "__main__":
    main()