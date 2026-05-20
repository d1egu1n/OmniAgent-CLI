import argparse
import sys

from colors import Fore, Style, init

from logger import Logger

# Importações dos módulos modulares
from file_manager import estatisticas_pasta, buscar_arquivo, organizar_arquivos
from analyzer import analisar_pasta
from system_ops import listar_arquivos_sistema, mostrar_diretorio_atual, ver_espaco_disco, executar_comando_sistema
from config_manager import mostrar_config, adicionar_palavra, remover_palavra, adicionar_extensao

# Inicializa o colorama no Windows
init()

def main() -> None:
    """Função principal que orquestra a interface CLI do Mini-Agente."""
    parser = argparse.ArgumentParser(
        description="Mini-Agente - Ferramenta modular para automação e análise de arquivos."
    )
    
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Comando: analisar
    p_analisar = subparsers.add_parser("analisar", help="Analisa arquivos de uma pasta em busca de palavras-chave")
    p_analisar.add_argument("pasta", type=str, help="Caminho da pasta a ser analisada")

    # Comando: organizar
    p_organizar = subparsers.add_parser("organizar", help="Organiza os arquivos de uma pasta por extensão")
    p_organizar.add_argument("pasta", type=str, help="Caminho da pasta a ser organizada")

    # Comando: buscar
    p_buscar = subparsers.add_parser("buscar", help="Busca por um arquivo específico")
    p_buscar.add_argument("nome", type=str, help="Nome ou parte do nome do arquivo")
    p_buscar.add_argument("pasta", type=str, help="Pasta onde será feita a busca")

    # Comando: estatisticas
    p_estatisticas = subparsers.add_parser("estatisticas", help="Exibe estatísticas dos tipos de arquivos em uma pasta")
    p_estatisticas.add_argument("pasta", type=str, help="Caminho da pasta")

    # Comando: historico
    subparsers.add_parser("historico", help="Exibe o histórico de logs do agente")

    # Comando: config
    p_config = subparsers.add_parser("config", help="Gerencia as configurações do agente")
    sub_config = p_config.add_subparsers(dest="acao_config", help="Ações de configuração")
    
    sub_config.add_parser("mostrar", help="Mostra as configurações atuais")
    
    p_add_palavra = sub_config.add_parser("add-palavra", help="Adiciona uma nova palavra-chave")
    p_add_palavra.add_argument("palavra", type=str, help="Palavra a ser adicionada")
    
    p_rm_palavra = sub_config.add_parser("rm-palavra", help="Remove uma palavra-chave")
    p_rm_palavra.add_argument("palavra", type=str, help="Palavra a ser removida")
    
    p_add_ext = sub_config.add_parser("add-extensao", help="Adiciona uma nova extensão suportada")
    p_add_ext.add_argument("ext", type=str, help="Extensão (ex: .log)")

    # Comando: sistema
    p_sistema = subparsers.add_parser("sistema", help="Executa operações no sistema operacional")
    sub_sistema = p_sistema.add_subparsers(dest="acao_sistema", help="Operações do sistema")
    
    p_listar = sub_sistema.add_parser("listar", help="Lista arquivos do sistema (dir/ls)")
    p_listar.add_argument("--pasta", type=str, default=".", help="Pasta para listar (padrão: atual)")
    
    sub_sistema.add_parser("pwd", help="Mostra o diretório atual de trabalho")
    
    sub_sistema.add_parser("disco", help="Mostra o uso de disco do sistema")
    
    p_executar = sub_sistema.add_parser("executar", help="Executa um comando livre no terminal")
    p_executar.add_argument("cmd", type=str, help="Comando a ser executado")

    # Processar argumentos
    args = parser.parse_args()

    if not args.comando:
        print(Fore.BLUE + "=== MINI-AGENTE ===" + Style.RESET_ALL)
        parser.print_help()
        return

    try:
        # Dispatcher - Mapeamento das ações
        if args.comando == "analisar":
            analisar_pasta(args.pasta)
            
        elif args.comando == "organizar":
            organizar_arquivos(args.pasta)
            
        elif args.comando == "buscar":
            buscar_arquivo(args.nome, args.pasta)
            
        elif args.comando == "estatisticas":
            estatisticas_pasta(args.pasta)
            
        elif args.comando == "historico":
            Logger.mostrar_historico()
            
        elif args.comando == "config":
            if args.acao_config == "mostrar":
                mostrar_config()
            elif args.acao_config == "add-palavra":
                adicionar_palavra(args.palavra)
            elif args.acao_config == "rm-palavra":
                remover_palavra(args.palavra)
            elif args.acao_config == "add-extensao":
                adicionar_extensao(args.ext)
            else:
                p_config.print_help()

        elif args.comando == "sistema":
            if args.acao_sistema == "listar":
                listar_arquivos_sistema(args.pasta)
            elif args.acao_sistema == "pwd":
                mostrar_diretorio_atual()
            elif args.acao_sistema == "disco":
                ver_espaco_disco()
            elif args.acao_sistema == "executar":
                executar_comando_sistema(args.cmd)
            else:
                p_sistema.print_help()

    except Exception as e:
        Logger.error("Falha Crítica na Execução", str(e))
        print(Fore.RED + f"Erro fatal: {e}" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
