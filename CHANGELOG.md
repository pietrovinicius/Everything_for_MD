# Changelog

## [0.1.3] - 2026-06-28
### Adicionado
- README.md com visão geral, pipeline, instalação, uso e padrões de desenvolvimento.
### Corrigido
- `.claude/settings.json`: hook Stop migrado para o schema `hooks` array (corrige erro do /doctor).

## [0.1.2] - 2026-06-27
### Adicionado
- MEMORY.md com memória completa do projeto.
- Hook de auto-push em `.claude/settings.json`.

## [0.1.1] - 2026-06-27
### Adicionado
- Anotacoes.txt com instruções de setup para macOS e Windows.

## [0.1.0] - 2026-06-27
### Adicionado
- Estrutura inicial do projeto (src/, tests/, assets/).
- Interface gráfica com CustomTkinter (upload, progresso, preview, salvar).
- Pipeline de conversão: Extractor (PyMuPDF) → Formatter → Converter.
- Configuração de projeto: pyproject.toml, requirements.txt, .gitignore.
