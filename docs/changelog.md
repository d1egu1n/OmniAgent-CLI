# Changelog

Todo tipo de mudança estrutural, adição de recursos e correção de falhas será registrado neste documento de acordo com a semântica padrão de versionamento ([Semantic Versioning](https://semver.org/)).

## [1.1.0] - 2026-05-17
### Added
- Extensa documentação na pasta `docs/` incluindo arquitetura, roadmap e troubleshooting para apoiar a escalabilidade open-source.
- Novo README principal com padronização visual em badges.
- Novo script de dependências `requirements.txt`.

### Changed
- Refatoração massiva da base de código do projeto antigo "Mini-Agente" transitando para o nome oficial OmniAgent CLI.
- Padronização em inglês para nomes de arquivos (ex: `file_manager.py`, `system_ops.py`) focando no padrão global.

## [1.0.0] - 2026-05-17
### Added
- Novo entry point via Interface de Linha de Comando usando o pacote `argparse`.
- Sistema global de logger via terminal com distinção de severidade através do uso do `Colorama` (INFO, WARNING, ERROR).
- Limite dinâmico rotativo de máximo 500 registros persistentes em JSON para poupar carga de I/O em discos do usuário.
- Type Hints do padrão Python >3.8 garantindo tipagem forte na manipulação de matrizes de dados.

### Fixed
- Loop infinito que provocava crash no sistema ao tentar organizar arquivos e se deparar com a duplicação de nome. (Implementado contador iterativo automático `_1, _2`).
- Corrigida fragilidade e crash iminente se `logs.json` apresentasse problema de decodificação (`json.JSONDecodeError`).

## [0.1.0] - 2026-05-09
### Added
- Lançamento inicial (Versão Alfa - Prova de Conceito).
- Motor interativo (via inputs e loop de menus).
- Execução bruta via `subprocess.run()`.
