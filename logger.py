import os
import json
from datetime import datetime
from colorama import Fore, Style

LOG_FILE = "logs.json"
MAX_LOGS = 500

class Logger:
    """Classe responsável pelo registro e exibição de histórico de execução."""

    @staticmethod
    def registrar_log(nivel: str, evento: str, detalhes: str = "") -> None:
        """
        Registra um log no arquivo JSON com níveis de severidade.
        Mantém o histórico limitado a MAX_LOGS registros.
        """
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = {
            "data": agora,
            "nivel": nivel.upper(),
            "evento": evento,
            "detalhes": detalhes
        }
        
        logs = []
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except Exception:
                logs = []

        logs.append(log)

        # Limitar o número de logs (mantém apenas os últimos)
        if len(logs) > MAX_LOGS:
            logs = logs[-MAX_LOGS:]

        try:
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(Fore.RED + f"Erro interno: Impossível salvar log em disco. {e}" + Style.RESET_ALL)

    @staticmethod
    def info(evento: str, detalhes: str = "") -> None:
        """Registra um evento de informação."""
        Logger.registrar_log("INFO", evento, detalhes)
        
    @staticmethod
    def warning(evento: str, detalhes: str = "") -> None:
        """Registra um aviso."""
        Logger.registrar_log("WARNING", evento, detalhes)
        
    @staticmethod
    def error(evento: str, detalhes: str = "") -> None:
        """Registra um erro."""
        Logger.registrar_log("ERROR", evento, detalhes)

    @staticmethod
    def mostrar_historico() -> None:
        """Exibe o histórico formatado e colorido no terminal, dependendo da severidade."""
        if not os.path.exists(LOG_FILE):
            print(Fore.RED + "Nenhum histórico encontrado!" + Style.RESET_ALL)
            return

        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)

            print(Fore.YELLOW + "\n=== HISTÓRICO DE EXECUÇÃO ===" + Style.RESET_ALL)

            for log in logs:
                nivel = log.get("nivel", "INFO")
                
                # Definição de cores baseada na severidade
                if nivel == "INFO":
                    cor_nivel = Fore.GREEN
                elif nivel == "WARNING":
                    cor_nivel = Fore.YELLOW
                elif nivel == "ERROR":
                    cor_nivel = Fore.RED
                else:
                    cor_nivel = Fore.WHITE

                data_str = log.get('data', 'Data Desconhecida')
                evento_str = log.get('evento', 'Evento Desconhecido')
                detalhes_str = log.get('detalhes', '')

                print(f"{Fore.CYAN}[{data_str}]{Style.RESET_ALL} {cor_nivel}[{nivel}]{Style.RESET_ALL}")
                print(f"Evento: {evento_str}")
                if detalhes_str:
                    print(f"Detalhes: {detalhes_str}")
                print("-" * 50)

        except Exception as e:
            print(Fore.RED + f"Erro ao ler histórico: {e}" + Style.RESET_ALL)
