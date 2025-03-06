# TPC3 (06/03/2025)
- Nome: Filipa Oliveira da Silva
- Número: A104167

![Foto](https://avatars.githubusercontent.com/u/144493282?v=4)

## Resumo
Este trabalho consiste na criação de um analisador léxico para uma linguagem de query.

## Funcionalidades
- **Identificação de Tokens:** O analisador reconhece e classifica diferentes elementos da linguagem, incluindo:
    - ***Palavras-chave*** (SELECT, WHERE, LIMIT);
    - ***Variáveis*** (?nome, ?desc);
    - ***Prefixos*** (dbo:MusicalArtist, foaf:name);
    - ***Strings*** ("Chuck Berry"@en);
    - ***Caracteres especiais*** ({, });
    - ***Números***;
    - ***Identificadores*** (s, w, dbo, foaf);
    - ***Erros*** (caracteres não reconhecidos);
    - ***Quebras de linha*** (\n).

## Implementação
O analisador léxico percorre a query caractere a caractere e aplica expressões regulares para classificar os tokens corretamente.

## Lista de Resultados
- [`analisador_lexico.py`](./analisador_lexico.py)

### Exemplo
- **Input**
```
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

- **Output**
```
('KEYWORD', 'select', 1, (0, 6))
('VARIABLE', '?nome', 1, (7, 12))
('VARIABLE', '?desc', 1, (13, 18))
('KEYWORD', 'where', 1, (19, 24))
('SPECIAL', '{', 1, (25, 26))
# ...
```