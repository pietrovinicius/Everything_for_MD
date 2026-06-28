# Everything for MD

Conversor desktop de **PDF → Markdown**. Faça upload de um PDF e receba o conteúdo em `.md`.

## Visão Geral

| Item | Detalhe |
|------|---------|
| **Stack** | Python 3.12+ |
| **UI** | Desktop GUI ([CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)) |
| **Motor** | [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`) |
| **Empacotamento** | PyInstaller (executável standalone `.app`/`.exe`) |
| **Versão** | `0.1.2` |

## Pipeline

```
PDF (input) → Extractor → PDFContent → Formatter → Markdown (output)
```

1. **Extractor** (`src/extractor.py`) — lê o PDF via PyMuPDF e extrai texto e blocos por página (`PDFContent` imutável).
2. **Formatter** (`src/formatter.py`) — converte `PDFContent` em string Markdown com título e marcação de páginas.
3. **Converter** (`src/converter.py`) — orquestra o pipeline, valida entrada e gerencia I/O.

## Instalação

```bash
# Clonar
git clone <repo-url>
cd Everything_for_MD

# Ambiente virtual
python -m venv venv
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate           # Windows

# Dependências
pip install -r requirements.txt
```

## Uso

```bash
# Rodar a GUI
python -m src.app
```

1. Selecione um arquivo PDF.
2. Acompanhe o progresso da conversão.
3. Visualize o preview e salve o `.md` gerado.

## Desenvolvimento

```bash
# Testes
pytest

# Lint / análise estática
ruff check .

# Type checking
mypy src/
```

### Padrões

- **Type Hints obrigatórios**, PEP8, Ruff como linter.
- **TDD** (Red-Green-Refactor) — teste com falha antes do código de produção.
- **Cobertura mínima:** 80%.
- **Imutabilidade:** retornar novos objetos, não mutar estado (`dataclass(frozen=True)`).

## Estrutura

```
Everything_for_MD/
├── src/
│   ├── app.py           # Entry point — instancia GUI e roda mainloop
│   ├── gui.py           # Interface CustomTkinter (upload, progresso, preview)
│   ├── converter.py     # Orquestra pipeline PDF → MD
│   ├── extractor.py     # Extração de texto/estrutura via PyMuPDF
│   └── formatter.py     # Formatação do conteúdo em Markdown
├── tests/               # Testes pytest (converter, extractor, formatter)
├── assets/              # Ícones e recursos visuais da GUI
├── output/              # Markdowns gerados (gitignored)
├── requirements.txt
├── pyproject.toml
├── CHANGELOG.md
└── CLAUDE.md
```

## Licença

Uso interno — Pietro Lima.
