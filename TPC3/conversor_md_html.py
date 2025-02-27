import re

def convert_headers(md):
    md = re.sub(r"^\s*# (.+)$", r"<h1>\1</h1>", md, flags=re.MULTILINE)
    md = re.sub(r"^\s*## (.+)$", r"<h2>\1</h2>", md, flags=re.MULTILINE)
    md = re.sub(r"^\s*### (.+)$", r"<h3>\1</h3>", md, flags=re.MULTILINE)
    return md

def convert_bold(md):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", md)

def convert_italic(md):
    return re.sub(r"(?<!\*)\*(.*?)\*(?!\*)", r"<i>\1</i>", md)

def convert_links(md):
    return re.sub(r"\[(.+?)\]\((https?:\/\/.+?)\)", r'<a href="\2">\1</a>', md)

def convert_images(md):
    return re.sub(r"!\[(.*?)\]\((https?:\/\/.+?)\)", r'<img src="\2" alt="\1"/>', md)

def convert_lists(md):
    lines = md.split("\n")
    html = []
    in_ol = False

    for line in lines:
        if match := re.match(r"^\s*\d+\.\s+(.+)$", line):
            if not in_ol:
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{match.group(1)}</li>")
        else:
            if in_ol:
                html.append("</ol>")
                in_ol = False
            html.append(line)

    if in_ol:
        html.append("</ol>")

    return "\n".join(html)

def md_to_html(md):
    md = convert_headers(md)
    md = convert_bold(md)
    md = convert_italic(md)
    md = convert_images(md)
    md = convert_links(md)
    md = convert_lists(md)
    return md

def main():
    markdown = """
    # Título
    ## Subtítulo
    ### Cabeçalho menor

    Este é um **exemplo** de negrito e este um *exemplo* de itálico.

    1. Primeiro item
    2. Segundo item
    3. Terceiro item

    Veja mais em [Google](https://www.google.com).

    Imagem abaixo:
    ![Imagem exemplo](https://www.exemplo.com/imagem.jpg)
    """
    
    html = md_to_html(markdown)
    print(html)

if __name__ == "__main__":
    main()  