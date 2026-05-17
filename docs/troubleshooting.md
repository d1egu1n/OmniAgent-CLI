# Troubleshooting Guide

Este guia lista problemas conhecidos que os administradores de sistemas podem enfrentar ao operar o **OmniAgent CLI** e como solucioná-los adequadamente.

## 1. Problemas de Permissão em Windows e Linux
**Sintoma:** Ao rodar `python main.py organizar ./C:/Windows` ou listar diretórios protegidos, o CLI devolve erros vermelhos de falha de leitura (como `PermissionError: [Errno 13] Permission denied`).
**Causa:** O Python herda os privilégios do terminal onde está rodando. O agente está tentando mexer em arquivos nativos do sistema.
**Solução:** 
- Em Windows: execute o `Powershell` ou `CMD` como Administrador.
- Em Linux/macOS: prefixe a sua chamada com `sudo`, ex: `sudo python main.py organizar /etc`.

## 2. Erros de Dependências Modulares (`ModuleNotFoundError`)
**Sintoma:** O CLI trava na primeira execução com erro: `ModuleNotFoundError: No module named 'colorama'`.
**Causa:** A máquina não possui as dependências externas registradas para o uso global.
**Solução:** Tenha certeza de instalar os pacotes obrigatórios descritos no seu arquivo de dependências:
```bash
pip install -r requirements.txt
```

## 3. O arquivo de LOGs JSON está em branco ou zerou
**Sintoma:** Você rodou o comando de histórico `python main.py historico` e nenhum dado foi mostrado.
**Causa:** O sistema de Auto-Recuperação apagou o log caso houvesse edição manual que invalidasse a estrutura do JSON.
**Solução:** O `logs.json` não deve ser alterado à mão (ou usando Editores de Texto corrompendo aspas). O agente automaticamente fará a higienização do arquivo em caso de decodificação falha, reiniciando o registro para manter estabilidade da ferramenta.

## 4. O Sistema de Organização falha sem mensagem explícita
**Sintoma:** O comando `organizar` reporta que fez o movimento, mas os arquivos desaparecem ou entram em conflito em redes não locais (ex: Pastas Sincronizadas do OneDrive).
**Causa:** `shutil.move()` pode enfrentar instabilidades se o destino for um disco diferente operando sob I/O intensivo sincronizado em nuvem.
**Solução:** Evite rodar o OmniAgent sob raízes controladas por Sincronizadores agressivos de Nuvem ou pause as sincronizações durante o comando.

## 5. Falha no Comando Livre (`sistema executar`)
**Sintoma:** Executar `python main.py sistema executar "ls -la"` gera falha se rodado no Windows.
**Causa:** O OmniAgent repassa o comando cru para o *Shell/Terminal* nativo. O Windows puro (CMD) não conhece nativamente o binário `ls`.
**Solução:** Garanta que você está requisitando comandos compatíveis com seu S.O subjacente (Use `dir` no Windows ou rode através do GitBash). Use os atalhos cross-plataforma encapsulados (`sistema listar`) para evitar problemas entre sistemas operacionais diferentes.
