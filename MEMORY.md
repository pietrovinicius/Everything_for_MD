# Everything for MD — Memória do Projeto

## Usuário
- Nome: Pietro Lima (desenvolvedor sênior)
- GitHub: pietrovinicius
- Máquina: MacBook Air (macOS Darwin 25.5.0)

## Projeto
- Repositório: https://github.com/pietrovinicius/Everything_for_MD
- Objetivo único: PDF in → Markdown out (desktop app)
- Stack: Python 3.12+, CustomTkinter (GUI), PyMuPDF (extração), PyInstaller (empacotamento futuro)
- Versão atual: 0.1.0
- Branch: main

## Estrutura Criada (v0.1.0)
```
src/app.py         → Entry point (mainloop)
src/gui.py         → CustomTkinter GUI (upload, progresso, preview, salvar)
src/converter.py   → Orquestra pipeline (valida → extrai → formata)
src/extractor.py   → PyMuPDF — extrai texto/blocos por página
src/formatter.py   → Converte PDFContent → string Markdown
tests/             → Vazio (próximo passo: TDD)
assets/            → Recursos visuais futuros
output/            → Markdowns gerados (gitignored)
```

## Decisões Técnicas
- Dataclasses imutáveis (frozen=True) para PDFContent e PageContent
- Pipeline: PDF → Extractor → Raw Content → Formatter → Markdown
- Riverpod/Flutter NÃO — isso é Python puro desktop
- Type hints obrigatórios, PEP8, Ruff linter, mypy strict
- TDD obrigatório: Red-Green-Refactor

## Configurações
- `pyproject.toml`: ruff (line-length=99, py312), mypy strict, pytest testpaths=["tests"]
- `requirements.txt`: customtkinter==5.2.2, PyMuPDF==1.25.1, pytest==8.3.4, ruff==0.8.6, mypy==1.14.1, pyinstaller==6.11.1
- `.gitignore`: output/*.md, build/, dist/, *.spec (exceto everything_for_md.spec)

## Git Workflow
- Commit message: `tipo: descrição em português (vX.Y.Z)`
- CHANGELOG.md: ordem decrescente, cada push = entrada versionada
- Push automático via hook Stop em `.claude/settings.json`

## Limitação Conhecida: Push via Claude Code
- O sandbox do Claude Code injeta variáveis de proxy (localhost:57043/57046)
- Essas variáveis bloqueiam conexão ao GitHub (HTTPS e SSH)
- Sem proxy, DNS não resolve (socket bind denied)
- **Solução:** Hook de Stop configurado — roda `git push` no shell do usuário fora do sandbox
- Commits locais são seguros; push feito pelo hook ou manualmente

## Commits Realizados
- `9e3047b` — feat: estrutura inicial do projeto com GUI CustomTkinter (v0.1.0)
- `932de57` — docs: adiciona instruções de setup para macOS e Windows (v0.1.0)

## Próximos Passos
1. Testes unitários (TDD) para extractor, formatter, converter
2. Melhorar formatação: detecção de headings, bold, listas, tabelas
3. PyInstaller .spec para gerar executável standalone
4. README.md com screenshots da GUI
