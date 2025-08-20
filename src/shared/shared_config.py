# src/shared/shared_config.py
import sys
import os

# garante que src esteja no sys.path mesmo quando executado diretamente
CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from system.config.config_file import DIRETORIO_RAIZ

print('DIRETORIO_RAIZ:', DIRETORIO_RAIZ)

variavel_shared = ''


# import sys, os

# # adiciona o diretório-pai (src), mas só dentro de shared
# CAMINHO_SYSTEM = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'system'))
# sys.path.append(CAMINHO_SYSTEM)
# from config.config_file import DIRETORIO_RAIZ as DIRETORIO_RAIZ
# sys.path.remove(CAMINHO_SYSTEM)
# del CAMINHO_SYSTEM


"""
def secure_import(from_value: str, import_value: str, as_value: str):
    CAMINHO_SYSTEM = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'system'))
    sys.path.append(CAMINHO_SYSTEM)
    from config.config_file import DIRETORIO_RAIZ as DIRETORIO_RAIZ
    sys.path.remove(CAMINHO_SYSTEM)
    del CAMINHO_SYSTEM
    return DIRETORIO_RAIZ


DIRETORIO_RAIZ = secure_import(from_value = 'config.config_file', import_value = 'DIRETORIO_RAIZ', as_value = 'DIRETORIO_RAIZ')
# """
