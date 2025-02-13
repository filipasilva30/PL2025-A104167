def somador_on_off(texto):
    soma = 0
    acumulador = 0
    ligado = True
    i = 0
    
    while i < len(texto):
        if i + 1 < len(texto) and texto[i:i+2].lower() == "on":
            ligado = True
            i += 2
            continue
        
        if i + 2 < len(texto) and texto[i:i+3].lower() == "off":
            ligado = False
            i += 3
            continue
        
        if texto[i] == "=":
            soma += acumulador
            return soma
        
        elif texto[i].isdigit() and ligado:
            acumulador = acumulador * 10 + int(texto[i])
        
        elif not texto[i].isdigit():
            soma += acumulador
            acumulador = 0
        
        i += 1
    
    return soma

def main():
    texto = input("Digite a sequência de entrada: ")
    resultado = somador_on_off(texto)
    print(resultado)

if __name__ == "__main__":
    main()