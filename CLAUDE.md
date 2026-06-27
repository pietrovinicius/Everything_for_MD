# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Everything for MD** é um conversor de PDF para Markdown (.md). O usuário faz upload de um arquivo PDF e recebe o conteúdo convertido em formato Markdown.

- **Stack:** Python 3.12+
- **Objetivo único:** PDF in → Markdown out
- **UI:** Desktop GUI (CustomTkinter)
- **Motor de conversão:** PyMuPDF (fitz)
- **Empacotamento:** PyInstaller (executável standalone .app/.exe)

## Common Commands

```bash
# Ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar testes
pytest

# Lint / análise estática
ruff check .

# Type checking
mypy src/
```

## Architecture

### Estrutura do Projeto

```
/Everything_for_MD/
├── src/
│   ├── __init__.py
│   ├── app.py              # Entry point — instancia GUI e roda mainloop
│   ├── gui.py              # Interface CustomTkinter (upload, progresso, preview)
│   ├── converter.py        # Orquestra pipeline PDF → MD
│   ├── extractor.py        # Extração de texto/estrutura via PyMuPDF
│   └── formatter.py        # Formatação do conteúdo extraído em Markdown
├── tests/
│   ├── __init__.py
│   ├── test_converter.py
│   ├── test_extractor.py
│   └── test_formatter.py
├── assets/                 # Ícones e recursos visuais da GUI
├── output/                 # Markdowns gerados (gitignored)
├── requirements.txt
├── pyproject.toml
├── everything_for_md.spec  # Config do PyInstaller (futuro)
├── CLAUDE.md
├── CHANGELOG.md
└── README.md
```

### Pipeline de Conversão

```
PDF (input) → Extractor → Raw Content → Formatter → Markdown (output)
```

1. **Extractor:** lê o PDF e extrai texto, headings, tabelas, imagens, links
2. **Formatter:** converte o conteúdo extraído em Markdown semanticamente correto
3. **Converter:** orquestra o pipeline e gerencia I/O

## Diretrizes de Desenvolvimento

### Comportamento de Escopo
- Antes de qualquer tarefa, identifique os arquivos **estritamente necessários**.
- Vá direto à implementação — Pietro é desenvolvedor Sênior.

### Padrões Técnicos
- **Python:** Type Hints obrigatórios, PEP8, Ruff como linter
- **Testes:** pytest, cobertura mínima 80%
- **Imutabilidade:** prefira retornar novos objetos, não mutar estado

### TDD Policy

Todo novo serviço ou lógica de negócio deve seguir Red-Green-Refactor:
1. Escreva o teste com falha em `tests/`
2. Implemente o mínimo de código para o teste passar
3. Refatore mantendo os testes verdes

## Princípios de Design

### 1. Think Before Coding

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them.
- If a simpler approach exists, say so.

### 2. Simplicity First

- Minimum code that solves the problem. Nothing speculative.
- No abstractions for single-use code.
- No "flexibility" that wasn't requested.

### 3. Surgical Changes

- Touch only what you must.
- Match existing style.
- Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

Transform tasks into verifiable goals:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
```

## Git Workflow

### Commit Message Format
```
<type>: <descrição em português> (vX.Y.Z)
```

Tipos: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`

### Após Cada Tarefa

```bash
git add <arquivos_modificados> CHANGELOG.md
git commit -m "tipo: descrição da mudança (vX.Y.Z)"
git push
```

## Política de CHANGELOG (OBRIGATÓRIO)

Após **toda** tarefa concluída (que gera um `git push`), atualizar o `CHANGELOG.md` na raiz do projeto.

### Regras:

1. **Ordem decrescente:** entradas mais recentes sempre no topo do arquivo.
2. **Cada entrada = um push versionado** com versão semântica e data.
3. **Formato de cada entrada:**

```markdown
## [X.Y.Z] - YYYY-MM-DD
### Adicionado | Corrigido | Alterado | Removido
- Descrição concisa da mudança.
```

4. **Nunca reordenar** entradas existentes — apenas inserir a nova no topo (abaixo do título do arquivo).
5. **O CHANGELOG.md deve ser commitado junto** com o código alterado no mesmo push.

### Exemplo:

```markdown
# Changelog

## [0.2.0] - 2026-06-28
### Adicionado
- Suporte a extração de tabelas do PDF.

## [0.1.1] - 2026-06-27
### Corrigido
- Encoding UTF-8 em PDFs com caracteres especiais.

## [0.1.0] - 2026-06-27
### Adicionado
- Pipeline inicial de conversão PDF → Markdown.
```

## Gestão de Contexto

- Ao concluir uma tarefa com sucesso, sugira: `💡 Use /compact antes da próxima solicitação.`
