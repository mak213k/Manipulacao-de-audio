import re
import pyttsx3
from pathlib import Path

# =====================================================
# Configurações
# =====================================================

ARQUIVO_TEXTO = "livro_extraido.txt"
ARQUIVO_SAIDA = "essencialismo_audio"

VELOCIDADE = 145
VOLUME = 1.0
MAX_CARACTERES = 2800

# =====================================================
# Inicialização da voz
# =====================================================

engine = pyttsx3.init()
engine.setProperty("rate", VELOCIDADE)
engine.setProperty("volume", VOLUME)

voices = engine.getProperty("voices")

for voice in voices:
    nome = voice.name.lower()

    if any(termo in nome for termo in ("maria", "brazil", "portuguese", "português")):
        engine.setProperty("voice", voice.id)
        break

# =====================================================
# Leitura sem limpeza ou alteração do conteúdo
# =====================================================

texto = Path(ARQUIVO_TEXTO).read_text(encoding="utf-8")

if not texto:
    raise ValueError("O arquivo de texto está vazio.")

# =====================================================
# Divisão em trechos, preservando o texto original
# =====================================================

def dividir_em_trechos(texto, limite=2800):
    # Identifica possíveis finais de frase sem remover caracteres.
    # A divisão ocorre quando depois da pontuação vem uma nova frase
    # iniciada por letra maiúscula ou pelo símbolo §.
    padrao = re.compile(
        r'[.!?](?:["”’\')\]]*)?(?=\s+(?:[A-ZÁÉÍÓÚÂÊÔÃÕÇ§]))'
    )

    partes = []
    inicio = 0

    for correspondencia in padrao.finditer(texto):
        fim = correspondencia.end()
        partes.append(texto[inicio:fim])
        inicio = fim

    if inicio < len(texto):
        partes.append(texto[inicio:])

    trechos = []
    atual = ""

    for parte in partes:
        # Não corta uma parte para caber no limite.
        # Se ela for maior que o limite, permanece inteira.
        if atual and len(atual) + len(parte) > limite:
            trechos.append(atual)
            atual = parte
        else:
            atual += parte

    if atual:
        trechos.append(atual)

    return trechos

trechos = dividir_em_trechos(texto, MAX_CARACTERES)

print(f"{len(trechos)} trechos encontrados.")

# =====================================================
# Geração dos áudios
# =====================================================

for indice, trecho in enumerate(trechos):
    nome_arquivo = f"{ARQUIVO_SAIDA}_{indice:03}.wav"
    print(f"Gerando trecho {indice + 1}/{len(trechos)}: {nome_arquivo}")
    engine.save_to_file(trecho, nome_arquivo)

engine.runAndWait()
engine.stop()

print("Concluído.")
