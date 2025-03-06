import re

TOKEN_REGEX = [
    (r"(?i)\bSELECT|WHERE|LIMIT\b", "KEYWORD"),  # Palavras-chave
    (r"\?[a-zA-Z_]\w*", "VARIABLE"),             # Variáveis (?nome, ?desc)
    (r"[a-zA-Z]+:[a-zA-Z]+", "PREFIX"),          # Prefixos (dbo:MusicalArtist)
    (r'"[^"]+"@[a-zA-Z]+', "STRING"),            # Strings com idioma ("Chuck Berry"@en)
    (r"[{}]", "SPECIAL"),                        # Caracteres especiais { }
    (r"\d+", "NUMBER"),                          # Números
    (r"[a-zA-Z.]+", "IDENTIFIER"),               # Identificadores 
    (r"\n", "NEWLINE"),                          # Quebra de linha
    (r"[ \t]+", "SKIP"),                         # Espaços e tabs
    (r".", "ERROR")                              # Qualquer outro caractere
]

def analisador(query):
    tokens = []
    pos = 0   # Posição na string
    line_num = 1  # Número da linha
    line_start = 0  # Posição inicial da linha

    while pos < len(query):
        match = None
        for pattern, token_type in TOKEN_REGEX:
            match = re.match(pattern, query[pos:])
            if match:
                start_pos = pos
                end_pos = pos + len(match.group(0))

                if token_type == "NEWLINE":
                    tokens.append((token_type, "\\n", line_num, (start_pos, end_pos)))
                    line_num += 1  # Incrementa o número da linha
                    line_start = end_pos  # Atualiza a posição inicial da nova linha
                elif token_type != "SKIP":  
                    tokens.append((token_type, match.group(0), line_num, (start_pos - line_start, end_pos - line_start)))

                pos = end_pos  # Avança a posição na string
                break

    return tokens

# Exemplo de uso
query = '''select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
'''

tokens = analisador(query)
for t in tokens:
    print(t)