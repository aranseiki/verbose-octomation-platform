import os
import sys

CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from datetime import datetime

from shared.shared_config import (
    DIRETORIO_RPA, criar_estrutura_log, registar_log,
    registar_log_decorator,
)

nome_automacao = os.path.basename(__file__).removesuffix('.py')

caminho_criado = criar_estrutura_log(
    data_hora=datetime.now(),
    cultura='pt_BR',
    diretorio_base=DIRETORIO_RPA,
)

# breakpoint()

registar_log(
    log_level='DEBUG',
    mensagem=f'Iniciando a automação {nome_automacao}',
    cultura='pt_BR.UTF-8',
    handler_name='root',
)
