import os
import json
from datetime import datetime
from colors import Fore, Style, init

LOG_FILE = "logs.json"
MAX_LOGS = 500

class Logger:
    """Classe responsável pelo registro e exibição de histórico de execução."""

    _logs_cache = None

    @classmethod
    def _carregar_logs(cls) -> None:
        """
        Carrega os logs do disco para a memória apenas uma vez.
        
        Caso o arquivo esteja corrompido, realiza a auto-recuperação
        inicializando o cache em branco e limpando o arquivo no disco.
        """
        if cls._logs_cache is not None:
            return
        
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    if isinstance(dados, list):
                        cls._logs_cache = dados
                    else:
                        cls._logs_cache = []
                        cls._salvar_logs()
            except Exception:
                cls._logs_cache = []
                cls._salvar_logs()
        else:
            cls._logs_cache = []

    @classmethod
    def _salvar_logs(cls) -> None:
        """Salva o cache de logs em disco."""
        try:
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump(cls._logs_cache, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(Fore.RED + f"Erro interno: Impossível salvar log em disco. {e}" + Style.RESET_ALL)

    @classmethod
    def registrar_log(cls, nivel: str, evento: str, detalhes: str = "") -> None:
        """
        Registra um log na memória e salva em disco.
        Mantém o histórico limitado a MAX_LOGS registros.
        """
        cls._carregar_logs()
        
        agora = datetime.now().isoformat()
        log = {
            "data": agora,
            "nivel": nivel.upper(),
            "evento": evento,
            "detalhes": detalhes
        }
        
        cls._logs_cache.append(log)

        # Limitar o número de logs (mantém apenas os últimos)
        if len(cls._logs_cache) > MAX_LOGS:
            cls._logs_cache = cls._logs_cache[-MAX_LOGS:]

        cls._salvar_logs()

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

    @classmethod
    def mostrar_historico(cls) -> None:
        """
        Exibe o histórico formatado e colorido no terminal, dependendo da severidade.
        
        Utiliza o cache carregado de forma resiliente.
        """
        cls._carregar_logs()

        if not cls._logs_cache:
            print(Fore.RED + "Nenhum histórico encontrado!" + Style.RESET_ALL)
            return

        print(Fore.YELLOW + "\n=== HISTÓRICO DE EXECUÇÃO ===" + Style.RESET_ALL)

        for log in cls._logs_cache:
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
