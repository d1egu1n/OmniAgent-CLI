import os
import json
from typing import Dict, List, Any
from logger import Logger

ARQUIVO_CONFIG = "config.json"

def carregar_config() -> Dict[str, Any]:
    """
    Carrega as configurações do arquivo JSON.
    Se o arquivo não existir, estiver corrompido ou contiver tipos inválidos,
    recria e salva os valores padrão em disco de forma resiliente.
    """
    config: Dict[str, Any] = {}
    config_corrompida = False

    if os.path.exists(ARQUIVO_CONFIG):
        try:
            with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, dict):
                    config = dados
                else:
                    config_corrompida = True
        except (json.JSONDecodeError, UnicodeDecodeError, Exception) as e:
            Logger.warning("Configuração corrompida no disco. Recriando padrão.", str(e))
            config_corrompida = True
    else:
        config_corrompida = True

    # Validação e recuperação de campos obrigatórios com tipos corretos
    palavras = config.get("palavras_alerta")
    if not isinstance(palavras, list):
        config["palavras_alerta"] = ["error", "fail", "warning"]
        config_corrompida = True
    else:
        # Garantir que todos os itens na lista são strings
        if not all(isinstance(item, str) for item in palavras):
            config["palavras_alerta"] = [str(item) for item in palavras]
            config_corrompida = True

    extensoes = config.get("extensoes_suportadas")
    if not isinstance(extensoes, list):
        config["extensoes_suportadas"] = [".txt", ".log", ".json", ".csv", ".md", ".py"]
        config_corrompida = True
    else:
        # Garantir que todos os itens na lista são strings
        if not all(isinstance(item, str) for item in extensoes):
            config["extensoes_suportadas"] = [str(item) for item in extensoes]
            config_corrompida = True

    # Salva a configuração padrão ou corrigida imediatamente se houver corrupção ou arquivo novo
    if config_corrompida or not os.path.exists(ARQUIVO_CONFIG):
        salvar_config(config)

    return config

def salvar_config(config: Dict[str, Any]) -> None:
    """Salva o dicionário de configurações no arquivo JSON."""
    try:
        with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        Logger.info("Configurações salvas com sucesso.")
    except Exception as e:
        Logger.error(f"Falha ao salvar configurações: {e}")

def mostrar_config() -> None:
    """Exibe no terminal as configurações atuais."""
    config = carregar_config()

    print("\n=== CONFIGURAÇÕES ===")

    print("\nPalavras de alerta:")
    for palavra in config.get("palavras_alerta", []):
        print(f"- {palavra}")

    print("\nExtensões suportadas:")
    for ext in config.get("extensoes_suportadas", []):
        print(f"- {ext}")

def adicionar_palavra(nova_palavra: str) -> None:
    """Adiciona uma nova palavra de alerta às configurações."""
    config = carregar_config()

    nova_palavra = nova_palavra.strip().lower()
    if not nova_palavra:
        print("Palavra não pode ser vazia.")
        return

    if nova_palavra not in config["palavras_alerta"]:
        config["palavras_alerta"].append(nova_palavra)
        salvar_config(config)
        print("Palavra adicionada com sucesso!")
        Logger.info(f"Palavra de alerta adicionada: {nova_palavra}")
    else:
        print("Essa palavra já existe!")

def remover_palavra(palavra: str) -> None:
    """Remove uma palavra de alerta existente nas configurações."""
    config = carregar_config()

    palavra = palavra.strip().lower()

    if palavra in config["palavras_alerta"]:
        config["palavras_alerta"].remove(palavra)
        salvar_config(config)
        print("Palavra removida!")
        Logger.info(f"Palavra de alerta removida: {palavra}")
    else:
        print("Palavra não encontrada!")

def adicionar_extensao(extensao: str) -> None:
    """Adiciona uma nova extensão suportada para análise."""
    config = carregar_config()

    extensao = extensao.strip().lower()
    if not extensao:
        print("Extensão não pode ser vazia.")
        return

    if not extensao.startswith("."):
        extensao = "." + extensao

    if extensao not in config["extensoes_suportadas"]:
        config["extensoes_suportadas"].append(extensao)
        salvar_config(config)
        print("Extensão adicionada!")
        Logger.info(f"Extensão suportada adicionada: {extensao}")
    else:
        print("Extensão já existe!")