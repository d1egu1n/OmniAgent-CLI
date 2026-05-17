import os
from typing import Dict
from colorama import Fore, Style
from logger import Logger
from config_manager import carregar_config
from file_manager import listar_arquivos, ler_arquivo

def buscar_palavras(texto: str, palavras: list) -> Dict[str, int]:
    """Retorna um dicionário com a contagem de ocorrência das palavras no texto."""
    resultados = {}
    for palavra in palavras:
        resultados[palavra] = texto.lower().count(palavra.lower())
    return resultados 

def analisar_pasta(pasta: str) -> None:
    """
    Percorre a pasta fornecida e analisa arquivos com extensões suportadas,
    procurando por palavras de alerta configuradas no JSON.
    """
    if not os.path.exists(pasta):
        msg = f"Pasta não encontrada para análise: {pasta}"
        print(Fore.RED + msg + Style.RESET_ALL)
        Logger.error("Análise falhou", msg)
        return

    config = carregar_config()
    palavras_alerta = config.get("palavras_alerta", [])
    extensoes_suportadas = config.get("extensoes_suportadas", [])

    if not palavras_alerta or not extensoes_suportadas:
        Logger.warning("Análise abortada", "Sem palavras de alerta ou extensões configuradas.")
        print(Fore.YELLOW + "Aviso: Sem palavras ou extensões configuradas para analisar." + Style.RESET_ALL)
        return

    arquivos = listar_arquivos(pasta)
    if not arquivos:
        print(Fore.YELLOW + "Pasta vazia ou sem acesso." + Style.RESET_ALL)
        return

    print("\nArquivos encontrados para análise:")
    arquivos_suportados = 0

    for arq in arquivos:
        caminho = os.path.join(pasta, arq)
        
        # Analisa apenas arquivos reais e que possuam a extensão correta
        if os.path.isfile(caminho) and any(arq.endswith(ext) for ext in extensoes_suportadas):
            arquivos_suportados += 1
            print(f"- {arq}")
            
            conteudo = ler_arquivo(caminho)
            if conteudo:
                resultado = buscar_palavras(conteudo, palavras_alerta)

                # Flag para saber se achou alguma palavra
                encontrou_algo = False
                for palavra, qtd in resultado.items():
                    if qtd > 0:
                        if not encontrou_algo:
                            print(Fore.CYAN + f"\nAnálise do arquivo: {arq}" + Style.RESET_ALL)
                            encontrou_algo = True
                            
                        print(f"  [{palavra}]: {qtd} vez(es)")
                        Logger.warning(f"Alerta: '{palavra}' encontrada", f"Arquivo: {arq} ({qtd} ocorrências)")

                Logger.info("Arquivo analisado", arq)

    if arquivos_suportados == 0:
        print(Fore.YELLOW + "\nNenhum arquivo com extensão suportada foi encontrado na raiz desta pasta." + Style.RESET_ALL)
        Logger.info("Análise concluída", "Nenhum arquivo suportado para analisar.")
    else:
        Logger.info("Análise de diretório finalizada", f"Pasta: {pasta}")
        print(Fore.GREEN + "\nAnálise concluída!" + Style.RESET_ALL)
