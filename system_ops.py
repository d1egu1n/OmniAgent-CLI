import os
import platform
import subprocess
from colors import Fore, Style, init
from logger import Logger

def listar_arquivos_sistema(pasta: str = ".") -> None:
    """Executa o comando nativo do sistema para listar arquivos."""
    sistema = platform.system()
    comando = "dir" if sistema == "Windows" else "ls -la"
    executar_comando_sistema(comando, pasta)

def mostrar_diretorio_atual() -> None:
    """Executa o comando nativo do sistema para mostrar o diretório atual."""
    sistema = platform.system()
    comando = "cd" if sistema == "Windows" else "pwd"
    executar_comando_sistema(comando)

def ver_espaco_disco() -> None:
    """Executa o comando nativo para checar o uso de disco."""
    sistema = platform.system()
    comando = "wmic logicaldisk get size,freespace,caption" if sistema == "Windows" else "df -h"
    executar_comando_sistema(comando)

def executar_comando_sistema(comando: str, cwd: str = ".") -> None:
    """
    Executa um comando no sistema operacional e registra no Logger.
    
    Seleciona dinamicamente a codificação adequada ("oem" para Windows,
    "utf-8" para outros sistemas) com substituição em caso de erro de decoding.
    """
    sistema = platform.system()
    codificacao = "oem" if sistema == "Windows" else "utf-8"

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            encoding=codificacao,
            errors="replace",
            cwd=cwd
        )

        if resultado.stdout:
            print(Fore.GREEN + "\n=== SAÍDA ===" + Style.RESET_ALL)
            print(resultado.stdout)
            Logger.info(f"Comando executado: {comando}", resultado.stdout.strip())

        if resultado.stderr:
            print(Fore.RED + "\n=== ERROR ===" + Style.RESET_ALL)
            print(resultado.stderr)
            Logger.error(f"Erro no comando: {comando}", resultado.stderr.strip())

    except Exception as e:
        erro_msg = f"Erro ao executar comando '{comando}': {e}"
        print(Fore.YELLOW + erro_msg + Style.RESET_ALL)
        Logger.error("Exceção na execução de comando", erro_msg)
