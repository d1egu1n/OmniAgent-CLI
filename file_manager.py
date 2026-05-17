import os
import shutil
from typing import List, Optional, Dict
from colorama import Fore, Style
from logger import Logger

def listar_arquivos(pasta: str) -> List[str]:
    """Retorna uma lista de nomes de todos os itens no diretório fornecido."""
    try:
        arquivos = os.listdir(pasta)
        return arquivos
    except Exception as e:
        Logger.error(f"Falha ao listar diretório '{pasta}'", str(e))
        print(Fore.RED + f"Erro ao listar arquivos: {e}" + Style.RESET_ALL)
        return []

def ler_arquivo(caminho: str) -> Optional[str]:
    """Lê o conteúdo de um arquivo de texto e retorna como string."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        Logger.warning(f"Não foi possível ler '{caminho}'", str(e))
        print(Fore.YELLOW + f"Aviso ao ler arquivo '{caminho}': {e}" + Style.RESET_ALL)
        return None

def estatisticas_pasta(pasta: str) -> None:
    """Gera estatísticas sobre os tipos de arquivos contidos recursivamente na pasta."""
    if not os.path.exists(pasta):
        msg = f"Pasta não encontrada: {pasta}"
        print(Fore.RED + msg + Style.RESET_ALL)
        Logger.error("Estatísticas falharam", msg)
        return

    total_arquivos = 0
    total_pastas = 0
    tipos_arquivo: Dict[str, int] = {}

    for raiz, pastas, arquivos in os.walk(pasta):
        total_pastas += len(pastas)
        total_arquivos += len(arquivos)

        for arquivo in arquivos:
            extensao = arquivo.split(".")[-1].lower() if "." in arquivo else "sem_extensao"
            tipos_arquivo[extensao] = tipos_arquivo.get(extensao, 0) + 1

    print(Fore.CYAN + "\n=== ESTATÍSTICAS ===" + Style.RESET_ALL)
    print(f"Arquivos: {total_arquivos}")
    print(f"Pastas: {total_pastas}")

    print(Fore.YELLOW + "\nTipos encontrados:" + Style.RESET_ALL)
    for tipo, quantidade in tipos_arquivo.items():
        print(f"{tipo.upper()}: {quantidade}")

    Logger.info("Estatísticas geradas", f"Analisada a pasta: {pasta}")

def buscar_arquivo(nome_arquivo: str, pasta: str) -> None:
    """Busca recursivamente por um arquivo que contenha 'nome_arquivo'."""
    if not os.path.exists(pasta):
        msg = f"Pasta não encontrada: {pasta}"
        print(Fore.RED + msg + Style.RESET_ALL)
        Logger.error("Busca falhou", msg)
        return

    encontrado = False

    for raiz, pastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if nome_arquivo.lower() in arquivo.lower():
                caminho_completo = os.path.join(raiz, arquivo)
                print(Fore.GREEN + "\nArquivo encontrado:" + Style.RESET_ALL)
                print(caminho_completo)
                
                Logger.info("Arquivo encontrado", caminho_completo)
                encontrado = True

    if not encontrado:
        print(Fore.RED + "Arquivo não encontrado!" + Style.RESET_ALL)
        Logger.warning("Busca de arquivo", f"Nenhum resultado para '{nome_arquivo}' em '{pasta}'")

def organizar_arquivos(pasta: str) -> None:
    """
    Organiza arquivos da pasta raiz em subdiretórios baseados em suas extensões.
    """
    if not os.path.exists(pasta):
        msg = f"Pasta não encontrada: {pasta}"
        print(Fore.RED + msg + Style.RESET_ALL)
        Logger.error("Organização falhou", msg)
        return

    arquivos = listar_arquivos(pasta)
    movidos = 0

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split(".")[-1].lower() if "." in arquivo else "sem_extensao"

            if extensao in ["jpg", "png", "jpeg"]:
                destino = os.path.join(pasta, "Imagens")
            elif extensao in ["pdf", "txt", "docx"]:
                destino = os.path.join(pasta, "Documentos")
            elif extensao in ["mp4", "mkv"]:
                destino = os.path.join(pasta, "Videos")
            else:
                destino = os.path.join(pasta, "Outros")

            os.makedirs(destino, exist_ok=True)

            novo_caminho = os.path.join(destino, arquivo)
            contador = 1
            nome_base, ext = os.path.splitext(arquivo)
            
            # Prevenir sobrescrita
            while os.path.exists(novo_caminho):
                novo_nome = f"{nome_base}_{contador}{ext}"
                novo_caminho = os.path.join(destino, novo_nome)
                contador += 1

            try:
                shutil.move(caminho_arquivo, novo_caminho)
                nome_final = os.path.basename(novo_caminho)
                print(Fore.GREEN + f"Arquivo movido: {arquivo} -> {nome_final}" + Style.RESET_ALL)
                Logger.info("Arquivo movido", f"{arquivo} -> {destino} ({nome_final})")
                movidos += 1
            except Exception as e:
                Logger.error(f"Falha ao mover arquivo '{arquivo}'", str(e))
                print(Fore.RED + f"Erro ao mover {arquivo}: {e}" + Style.RESET_ALL)

    if movidos == 0:
        print(Fore.YELLOW + "Nenhum arquivo para mover." + Style.RESET_ALL)
