Mayko, aqui está o README completo atualizado com as tarefas que os três scripts realizam e que não estavam documentadas.

<artifact id="readme-pdf-to-speech" type="markdown" title="README - PDF to Speech (atualizado)">
# 📚 PDF to Speech

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Text to Speech](https://img.shields.io/badge/Text--to--Speech-pyttsx3-success)
![PDF](https://img.shields.io/badge/PDF-pypdf-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Converta automaticamente documentos **PDF** em arquivos de áudio utilizando Python.

O projeto agora está organizado em um **pipeline de duas etapas**: primeiro o texto é extraído do PDF e salvo em um arquivo `.txt`; depois, esse texto é convertido em áudio. Uma versão original, que executa o fluxo completo em um único script, também é mantida no repositório.

A extração gera relatórios de páginas com problemas, o texto extraído é preservado sem limpeza, e a divisão em trechos respeita finais de frase — sem cortar palavras no meio.

---

# 🎯 Objetivo

Automatizar a conversão de livros, apostilas e documentos PDF em áudio para facilitar:

- 📖 Estudos
- 🎧 Audiobooks
- ♿ Acessibilidade
- 🚗 Escutar conteúdos durante deslocamentos

---

# ✨ Funcionalidades

## Etapa 1 — Extração do texto (`pdf_to_txt.py`)

- ✅ Extração automática de texto de arquivos PDF
- ✅ Extração em etapa separada, salvando o resultado em arquivo `.txt`
- ✅ Tolerância a PDFs malformados (`strict=False` no `pypdf`)
- ✅ Tratamento individual de erros por página (a falha em uma página não interrompe o processo)
- ✅ Relatório de páginas com erro de extração
- ✅ Relatório de páginas sem texto extraível
- ✅ Validação da existência do arquivo PDF antes de processar
- ✅ Feedback do progresso página a página no terminal
- ✅ Uso de `pathlib.Path` para manipulação segura de caminhos

## Etapa 2 — Conversão em áudio (`texto_voz_2.py`)

- ✅ Leitura direta de arquivos `.txt` com codificação UTF-8
- ✅ Preservação integral do texto original (sem limpeza ou alteração de conteúdo)
- ✅ Divisão em trechos respeitando finais de frase (pontuação seguida de letra maiúscula ou `§`)
- ✅ Não corta uma frase ao meio: se um trecho excede o limite, ele é mantido inteiro
- ✅ Validação de texto vazio (`raise ValueError` se o arquivo estiver vazio)
- ✅ Seleção automática de voz em português (quando disponível)
- ✅ Controle de velocidade da fala
- ✅ Controle de volume
- ✅ Geração de múltiplos arquivos WAV com índice sequencial (`_000`, `_001`, ...)

## Versão original (`texto_voz.py`)

- ✅ Extração de texto de PDF e conversão em áudio em um único script
- ✅ Limpeza e normalização do texto
- ✅ Remoção de hifenização
- ✅ Junção de linhas e remoção de espaços duplicados
- ✅ Inserção de pausas artificiais em pontuações e símbolos
- ✅ Criação automática da pasta de destino
- ✅ Movimentação do PDF original para a pasta de saída após a conversão

---

# 🏗️ Fluxo da aplicação

## Pipeline recomendado (duas etapas)

```text
Etapa 1: pdf_to_txt.py
PDF
 │
 ▼
Extração página por página
 │
 ▼
Tratamento de erros e relatório
 │
 ▼
livro_extraido.txt


Etapa 2: texto_voz_2.py
livro_extraido.txt
 │
 ▼
Leitura preservando o original
 │
 ▼
Divisão em trechos por frases
 │
 ▼
Síntese de Voz
 │
 ▼
Arquivos WAV
```

## Fluxo original (uma etapa)

```text
PDF
 │
 ▼
Extração do Texto
 │
 ▼
Limpeza e Normalização
 │
 ▼
Divisão em Blocos
 │
 ▼
Síntese de Voz
 │
 ▼
Arquivos WAV
```

---

# 📂 Estrutura do projeto

```text
.
├── pdf_to_txt.py          # Etapa 1: extrai texto do PDF e salva em .txt
├── texto_voz_2.py         # Etapa 2: converte .txt em áudio (preserva o original)
├── texto_voz.py           # Versão original: PDF → WAV em um único script
├── livro_extraido.txt     # Texto extraído (gerado pela Etapa 1)
├── README.md
└── .gitignore
```

---

# ⚙️ Tecnologias

- Python
- pyttsx3
- pypdf
- pathlib
- Expressões Regulares (Regex)

---

# 📦 Instalação

Clone o projeto

```bash
git clone https://github.com/mak213k/Manipulacao-de-audio.git
```

Entre na pasta

```bash
cd Manipulacao-de-audio
```

Instale as dependências

```bash
pip install pyttsx3 pypdf
```

---

# 🚀 Como utilizar

## Pipeline recomendado (duas etapas)

### 1º Extraia o texto do PDF

Configure o arquivo PDF e o nome do arquivo de saída no `pdf_to_txt.py`:

```python
NOME_PDF = "meu_livro.pdf"
ARQUIVO_TXT = "livro_extraido.txt"
```

Execute:

```bash
python pdf_to_txt.py
```

Saída esperada:

```text
Lendo o arquivo: meu_livro.pdf
Processando página 1 de 200...
Processando página 2 de 200...
...
Concluído. Texto salvo em: livro_extraido.txt
Páginas com erro de extração: []
Páginas sem texto extraível: [45, 46]
```

### 2º Converta o texto em áudio

Configure o arquivo de texto e o prefixo dos áudios no `texto_voz_2.py`:

```python
ARQUIVO_TEXTO = "livro_extraido.txt"
ARQUIVO_SAIDA = "essencialismo_audio"
```

Execute:

```bash
python texto_voz_2.py
```

Ao final da execução serão gerados os arquivos:

```text
essencialismo_audio_000.wav
essencialismo_audio_001.wav
essencialismo_audio_002.wav
...
```

## Fluxo original (uma etapa)

Configure o arquivo PDF e o nome de saída no `texto_voz.py`:

```python
NOME_PDF = "arquivo.pdf"
ARQUIVO_SAIDA = "livro"
```

Execute:

```bash
python texto_voz.py
```

---

# ⚙️ Configurações

| Parâmetro | Script | Descrição |
|-----------|--------|-----------|
| `NOME_PDF` | `pdf_to_txt.py`, `texto_voz.py` | Documento de entrada |
| `ARQUIVO_TXT` | `pdf_to_txt.py` | Nome do arquivo `.txt` gerado na extração |
| `ARQUIVO_TEXTO` | `texto_voz_2.py` | Arquivo `.txt` de entrada para conversão |
| `ARQUIVO_SAIDA` | `texto_voz.py`, `texto_voz_2.py` | Prefixo dos arquivos WAV |
| `VELOCIDADE` | `texto_voz.py`, `texto_voz_2.py` | Velocidade da fala |
| `VOLUME` | `texto_voz.py`, `texto_voz_2.py` | Volume do áudio |
| `MAX_CARACTERES` | `texto_voz.py`, `texto_voz_2.py` | Tamanho máximo de cada trecho/bloco |

---

# 🧠 Como funciona

## Pipeline recomendado

O processamento ocorre em duas etapas independentes:

1. **Extração do texto** (`pdf_to_txt.py`): lê o PDF página a página, captura erros por página e salva o texto bruto em um arquivo `.txt`, informando quais páginas não puderam ser processadas.
2. **Conversão em áudio** (`texto_voz_2.py`): lê o `.txt` sem alterar o conteúdo, divide o texto em trechos respeitando finais de frase e converte cada trecho em um arquivo WAV.

## Fluxo original

O processamento ocorre em quatro etapas:

1. Extração do texto do PDF;
2. Limpeza e padronização utilizando expressões regulares;
3. Divisão do conteúdo em blocos menores para evitar limitações do sintetizador;
4. Conversão de cada bloco em um arquivo de áudio.

---

# 💡 Possíveis melhorias

- [ ] Interface gráfica (Tkinter ou CustomTkinter)
- [ ] Exportação para MP3
- [ ] Barra de progresso
- [ ] Seleção de páginas do PDF
- [ ] Escolha manual da voz
- [ ] Suporte a múltiplos idiomas
- [ ] Conversão em lote de vários PDFs

---

# 🎓 Casos de uso

- Criação de audiobooks
- Conversão de apostilas
- Leitura de artigos científicos
- Estudos durante deslocamentos
- Recursos de acessibilidade

---

# 👨‍💻 Autor

**Mayko Costa**

- GitHub: https://github.com/mak213k
- LinkedIn: https://www.linkedin.com/in/maykocosta/
- Kaggle: https://www.kaggle.com/makrrc

---

# ⭐ Gostou do projeto?

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório.
</artifact>

As principais adições foram: **extração em etapa separada com relatório de páginas com erro/sem texto**, **preservação do texto original na conversão**, **divisão que não corta frases ao meio**, **validação de arquivos vazios** e **criação/movimentação automática de pastas** no fluxo original. O README agora reflete o pipeline real de dois scripts mais a versão legada.