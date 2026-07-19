import re
import pyttsx3
from pypdf import PdfReader

# =====================================================
# Configurações
# =====================================================

NOME_PDF = "Pag35_Aurélien Géron - Mãos à Obra_ Aprendizado de Máquina com Scikit-Learn & TensorFlow (2019).pdf"
ARQUIVO_SAIDA = "livro_final"

VELOCIDADE = 145
VOLUME = 1.0
MAX_CARACTERES = 2800

# =====================================================
# Inicialização
# =====================================================

engine = pyttsx3.init()

engine.setProperty("rate", VELOCIDADE)
engine.setProperty("volume", VOLUME)

# =====================================================
# Escolher melhor voz
# =====================================================

voices = engine.getProperty("voices")

for voice in voices:
    nome = voice.name.lower()

    if ("maria" in nome or
        "brazil" in nome or
        "portuguese" in nome or
        "português" in nome):
        engine.setProperty("voice", voice.id)
        break

# =====================================================
# Limpeza do texto
# =====================================================

def limpar_texto(texto):

    # Remove hifenização
    texto = re.sub(r'-\n', '', texto)

    # Junta linhas
    texto = re.sub(r'\n+', '\n', texto)

    texto = texto.replace("\n", " ")

    # Remove espaços duplicados
    texto = re.sub(r'\s+', ' ', texto)

    # Pequenas pausas artificiais
    texto = texto.replace(".", ". ")
    texto = texto.replace(",", ", ")
    texto = texto.replace(";", "; ")
    texto = texto.replace(":", ": ")
    texto = texto.replace("!", "! ")
    texto = texto.replace("?", "? ")
    texto = texto.replace("(", "( ")
    texto = texto.replace(")", " )")
    texto = texto.replace("[", "[ ")
    texto = texto.replace("]", " ]")
    texto = texto.replace("{", "{ ")
    texto = texto.replace("}", " }")
    texto = texto.replace("-", "- ")
    texto = texto.replace("—", " — ")
    texto = texto.replace("...", "... ")
    texto = texto.replace("“", " “ ")
    texto = texto.replace("”", " ” ")
    texto = texto.replace("‘", " ‘ ")
    texto = texto.replace("’", " ’ ")
    texto = texto.replace('"', ' " ')
    texto = texto.replace("'", " ' ")
    texto = texto.replace("  ", " ")
    texto = texto.replace("_", " _ ")

    return texto.strip()

# =====================================================
# Extrai PDF
# =====================================================

print("Extraindo texto...")

reader = PdfReader(NOME_PDF)

texto = ""

for pagina in reader.pages:

    conteudo = pagina.extract_text()

    if conteudo:
        texto += conteudo + "\n"

texto = limpar_texto(texto)

if texto == "":
    print("Nenhum texto encontrado.")
    exit()

# =====================================================
# Divide por frases
# =====================================================

def dividir_em_blocos(texto, limite=2800):

    frases = re.split(r'(?<=[.!?])\s+', texto)

    blocos = []

    atual = ""

    for frase in frases:

        if len(atual) + len(frase) < limite:

            atual += frase + " "

        else:

            blocos.append(atual.strip())
            atual = frase + " "

    if atual:
        blocos.append(atual.strip())

    return blocos

blocos = dividir_em_blocos(texto, MAX_CARACTERES)

print(f"{len(blocos)} blocos encontrados.")

# =====================================================
# Geração do áudio
# =====================================================

for indice, bloco in enumerate(blocos):

    print(f"Gerando bloco {indice+1}/{len(blocos)}")

    nome = f"{ARQUIVO_SAIDA}_{indice:03}.wav"

    engine.save_to_file(bloco, nome)

engine.runAndWait()
engine.stop()

print("Concluído.")