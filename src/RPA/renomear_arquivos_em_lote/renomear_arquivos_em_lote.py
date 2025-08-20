import sys
import os

CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from shared import variavel_shared, DIRETORIO_RAIZ

# from shared.shared_config import
# config.DIRETORIO_RAIZ

# from utils.logger_utils import registar_log

# registar_log(
#     log_level='DEBUG',
#     mensagem=f'Iniciando a automação {__name__.removeprefix('.py')}',
#     cultura='pt_BR.UTF-8',
#     handler_name='root',
# )
