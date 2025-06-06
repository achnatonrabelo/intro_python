import os

import datetime

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time() -> datetime:
    agora = datetime.datetime.now()
    return agora