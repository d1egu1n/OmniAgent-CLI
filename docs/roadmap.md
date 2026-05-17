# Roadmap

Nosso objetivo é transformar a ferramenta **OmniAgent CLI** de um utilitário local para um ecossistema completo de automação corporativa e análise forense de dados. O projeto está divido em *Milestones* (marcos de evolução).

## Fase 1: Fundação (Status: Concluído ✅)
- [x] Migração de scripts espaguetes para uma CLI modular baseada em `argparse`.
- [x] Implementação de sistema de Logs (`logger.py`) com persistência em JSON.
- [x] Modularização completa com injeção de configurações (`config_manager.py`).
- [x] Refatoração de Clean Code (Type Hinting e Docstrings).

## Fase 2: Robustez e Extensibilidade (Status: Planejado 🗓️)
- [ ] **Integração Pytest:** Adoção de TDD (Test-Driven Development) cobrindo todos os módulos core. Cobertura de código almejada de 90%+.
- [ ] **Motor de Busca Avançado:** Integração nativa de buscas baseadas em Expressões Regulares (Regex) em `analyzer.py`.
- [ ] **Manipulação Multi-formato:** Extração de conteúdo bruto de arquivos `.pdf`, `.docx` e `.xlsx` para ampliar o espectro do analisador.
- [ ] **Publicação PyPI:** Transformar o projeto em um pacote oficial Python com `setup.py` permitindo instalação global `pip install omni-agent`.

## Fase 3: Operações Distribuídas (Status: Visão de Futuro 🚀)
- [ ] **Hooks de Alerta:** Envio proativo de logs de criticidade `ERROR` para webhooks externos (Slack, Discord, Microsoft Teams).
- [ ] **Plugins e Extensões:** Arquitetura baseada em plugins que permitirá aos usuários criarem seus próprios módulos Python customizados que se ligam ao orquestrador nativo.
- [ ] **Daemon Mode (Background):** Serviço em segundo-plano (SystemD/Windows Services) monitorando diretórios em tempo real (ex: com `Watchdog`) organizando arquivos automaticamente no momento que são baixados.
- [ ] **Relatórios Inteligentes (IA):** Chamadas agendadas conectadas à APIs de LLMs para gerar relatórios resumidos de grandes massas de arquivos analisados.
