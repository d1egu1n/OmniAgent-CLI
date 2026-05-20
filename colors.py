"""
Módulo de cores do OmniAgent-CLI.

Fornece suporte à biblioteca colorama se instalada,
caindo de volta para valores vazios seguros caso não esteja disponível,
evitando assim quebras em ambientes que não possuem dependências externas.
"""

try:
    import colorama
    from colorama import init, Fore, Style
except ImportError:
    class Fore:
        """Stubs para Fore da biblioteca colorama."""
        BLUE: str = ""
        RED: str = ""
        GREEN: str = ""
        YELLOW: str = ""
        CYAN: str = ""
        WHITE: str = ""

    class Style:
        """Stubs para Style da biblioteca colorama."""
        RESET_ALL: str = ""

    def init() -> None:
        """Stub para a função init do colorama."""
        pass
