# 📚 PDF to Speech

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Text to Speech](https://img.shields.io/badge/Text--to--Speech-pyttsx3-success)
![PDF](https://img.shields.io/badge/PDF-pypdf-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Converta automaticamente documentos **PDF** em arquivos de áudio utilizando Python.

O projeto realiza a extração do texto, faz uma limpeza inteligente do conteúdo, divide textos longos em blocos menores e gera arquivos `.wav` utilizando um mecanismo de síntese de voz local.

---

# 🎯 Objetivo

Automatizar a conversão de livros, apostilas e documentos PDF em áudio para facilitar:

- 📖 Estudos
- 🎧 Audiobooks
- ♿ Acessibilidade
- 🚗 Escutar conteúdos durante deslocamentos

---

# ✨ Funcionalidades

- ✅ Extração automática de texto de arquivos PDF
- ✅ Limpeza e normalização do texto
- ✅ Remoção de hifenização
- ✅ Organização de parágrafos
- ✅ Seleção automática de voz em português (quando disponível)
- ✅ Controle de velocidade da fala
- ✅ Controle de volume
- ✅ Divisão inteligente em blocos para textos longos
- ✅ Geração de múltiplos arquivos WAV

---

# 🏗️ Fluxo da aplicação

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
├── texto_voz.py
├── README.md
└── .gitignore
```

---

# ⚙️ Tecnologias

- Python
- pyttsx3
- pypdf
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

Configure o arquivo PDF no início do script:

```python
NOME_PDF = "arquivo.pdf"
```

Defina o nome dos arquivos de saída:

```python
ARQUIVO_SAIDA = "livro"
```

Execute:

```bash
python texto_voz.py
```

Ao final da execução serão gerados arquivos:

```text
livro_000.wav
livro_001.wav
livro_002.wav
...
```

---

# ⚙️ Configurações

O script permite personalizar facilmente alguns parâmetros:

| Parâmetro | Descrição |
|-----------|-----------|
| `VELOCIDADE` | Velocidade da fala |
| `VOLUME` | Volume do áudio |
| `MAX_CARACTERES` | Tamanho máximo de cada bloco |
| `NOME_PDF` | Documento de entrada |
| `ARQUIVO_SAIDA` | Prefixo dos arquivos WAV |

---

# 🧠 Como funciona

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
