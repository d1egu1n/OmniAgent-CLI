<div align="center">
  <h1>🛡️ OmniAgent CLI</h1>
  <p><strong>A modular and resilient file automation and intelligence engine.</strong></p>

  <!-- Badges Profissionais -->
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python Version"/></a>
  <a href="https://github.com/d1egu1n/mini-log-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Architecture-Clean_Code-orange.svg?style=flat-square" alt="Clean Code"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Active-success.svg?style=flat-square" alt="Status"/></a>
</div>

<br/>

O **OmniAgent CLI** (sucessor do projeto "Mini-Agente") é uma poderosa interface de linha de comando voltada para automação de tarefas de S.O., organização avançada de diretórios, coleta de estatísticas em disco e varredura de dados baseados em alerta (Data Scanning). 

Criado com foco absoluto em modularidade e *Clean Code*, ele se comporta como uma ferramenta profissional de gestão e telemetria, não devendo nada às ferramentas oficiais dos ambientes Unix.

## 🚀 Guia de Uso Rápido (Quickstart)

**1. Instalação de Dependências**
```bash
pip install -r requirements.txt
```

**2. Listar todos os comandos disponíveis**
```bash
python main.py -h
```

**3. Exemplos Reais**
```bash
# Executa uma varredura buscando palavras configuradas na pasta atual
python main.py analisar .

# Organiza automaticamente a bagunça de uma pasta de Downloads por tipo de arquivo
python main.py organizar "C:\Users\EDSON\Downloads"

# Busca a localização exata de um arquivo perdido
python main.py buscar "fatura.pdf" "C:\Users\EDSON\Documentos"

# Exibe histórico colorido de todas as execuções recentes com níveis de log
python main.py historico
```

## 🏗️ Estrutura do Projeto

Abaixo a visão holística dos arquivos fundamentais da arquitetura. Leia o [architecture.md](docs/architecture.md) para aprofundamento de design de software.

```text
omni-agent/
│
├── docs/                      # 📚 Toda documentação especializada
│   ├── architecture.md        # Responsabilidade de cada módulo e diagrama
│   ├── roadmap.md             # Funcionalidades e visões do futuro do OmniAgent
│   ├── changelog.md           # Log histórico de mudanças baseadas em SemVer
│   └── troubleshooting.md     # Guia prático de resoluções de problemas (Permissões, etc)
│
├── main.py                    # 🚦 Entry point e roteador CLI nativo via argparse
├── analyzer.py                # 🔍 Motor inteligente de busca (Forensics / Alertas)
├── logger.py                  # 📝 Módulo singleton de telemetria colorida e JSON IO
├── file_manager.py            # 📁 Envelopa leitura, listagem, e operações de movimentação
├── config_manager.py          # ⚙️ Módulo de manipulação de parâmetros (Estado Global)
├── system_ops.py              # 💻 Interações subjacentes de S.O (Subprocesses / Espaço Disco)
├── logs.json                  # Data Storage auto-limitado a 500 registros das operações
├── config.json                # Configurações do usuário (Palavras e Extensões)
└── requirements.txt           # Declaração das dependências do ambiente Python
```

## 📚 Documentação (Docs)

Nossa documentação corporativa fica contida na sub-pasta `docs/`. Recomendamos forte leitura para contribuidores:
- **[Arquitetura e Fluxo (Architecture)](docs/architecture.md)**
- **[Futuro da Ferramenta (Roadmap)](docs/roadmap.md)**
- **[Logs de Versões (Changelog)](docs/changelog.md)**
- **[Guia de Erros Comuns (Troubleshooting)](docs/troubleshooting.md)**

---
<p align="center">Construído com ❤️ para automatizar as dores diárias de file-management.</p>
