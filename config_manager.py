import json
from typing import Dict, List, Any
from logger import Logger

ARQUIVO_CONFIG = "config.json"

def carregar_config() -> Dict[str, Any]:
    """
    Carrega as configurações do arquivo JSON.
    Se o arquivo não existir ou estiver corrompido, recria com valores padrão.
    """
    try:
        with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        Logger.warning("Configuração ausente ou corrompida. Criando padrão.")
        config_padrao = {
            "palavras_alerta": [
                "error",
                "fail",
                "warning"
            ],
            "extensoes_suportadas": [
                ".txt",
                ".log",
                ".json",
                ".csv",
                ".md",
                ".py"
            ]
        }
        salvar_config(config_padrao)
        return config_padrao

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