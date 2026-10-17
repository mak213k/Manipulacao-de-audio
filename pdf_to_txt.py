from pathlib import Path
from pypdf import PdfReader

# =====================================================
# Configurações
# =====================================================

NOME_PDF = "Mundo_Assombrado_pelos_Demonios_Carl_Sagan.pdf"
ARQUIVO_TXT = "livro_extraido.txt"

# =====================================================
# Extração do texto
# =====================================================

caminho_pdf = Path(NOME_PDF)
caminho_txt = Path(ARQUIVO_TXT)

if not caminho_pdf.exists():
    raise FileNotFoundError(f"Arquivo PDF não encontrado: {caminho_pdf}")

print(f"Lendo o arquivo: {caminho_pdf}")

reader = PdfReader(str(caminho_pdf), strict=False)

textos = []
paginas_com_erro = []
paginas_sem_texto = []

for numero, pagina in enumerate(reader.pages, start=1):
    print(f"Processando página {numero} de {len(reader.pages)}...")

    try:
        conteudo = pagina.extract_text()
    except Exception as erro:
        print(f"Não foi possível extrair a página {numero}: {erro}")
        paginas_com_erro.append(numero)
        continue

    if conteudo:
        textos.append(conteudo)
    else:
        paginas_sem_texto.append(numero)

# Mantém o texto extraído de cada página sem aplicar limpeza.
texto_final = "\n".join(textos)

with open(caminho_txt, "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_final)

print(f"\nConcluído. Texto salvo em: {caminho_txt.resolve()}")

if paginas_com_erro:
    print(f"Páginas com erro de extração: {paginas_com_erro}")

if paginas_sem_texto:
    print(f"Páginas sem texto extraível: {paginas_sem_texto}")
