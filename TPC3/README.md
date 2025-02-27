# TPC3 (27/02/2025)
- Nome: Filipa Oliveira da Silva
- Número: A104167

![Foto](https://avatars.githubusercontent.com/u/144493282?v=4)

## Resumo
Este trabalho consiste no desenvolvimento de um pequeno conversor de MarkDown para HTML, que processa elementos básicos da sintaxe MarkDown e converte-os para os equivalentes em HTML.

## Funcionalidades
- **Cabeçalhos**: conversão de `#`,`##` e `###` para `<h1>`, `<h2>` e `<h3>`, respetivamente.
- **Negrito**: conversão de `**texto**` para `<b>texto</b>`.
- **Itálico**: conversão de `*texto*` para `<i>texto</i>`.
- **Listas Numeradas**: conversão de, por exemplo, `(1. item)` para `<ol><li>item</li></ol>`.
- **Links**: conversão de `[texto](url)` para `<a href="url">texto</a>`.
- **Imagens**: conversão de `![alt](url)` para `<img src="url" alt="alt"/>`.

## Implementação
É feito um método para a conversão de cada uma das funcionalidades descritas acima.

## Lista de Resultados
- [`conversor_md_html.py`](./conversor_md_html.py)

### Exemplo
- **Input**
```
# Título

Este é um **exemplo** de negrito e este um *exemplo* de itálico.

1. Primeiro item
2. Segundo item
3. Terceiro item

Veja mais em [Google](https://www.google.com).

Imagem abaixo:
![Imagem exemplo](https://www.exemplo.com/imagem.jpg)
```

- **Output**
```
    <h1>Título</h1>
    <h2>Subtítulo</h2>
    <h3>Cabeçalho menor</h3>

    Este é um <b>exemplo</b> de negrito e este um <i>exemplo</i> de itálico.

    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>

    Veja mais em <a href="https://www.google.com">Google</a>.

    Imagem abaixo:
    <img src="https://www.exemplo.com/imagem.jpg" alt="Imagem exemplo"/>
```
