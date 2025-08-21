import os
import sys

CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from datetime import datetime
from json import load
from pathlib import Path

from shared.shared_config import (
    DIRETORIO_RPA,
    criar_estrutura_log,
    registar_log,
    registar_log_decorator,
)

NOME_AUTOMACAO = os.path.basename(__file__).removesuffix('.py')
DIRETORIO_PROJETO = DIRETORIO_RPA / NOME_AUTOMACAO
DIRETORIO_CONFIG = DIRETORIO_PROJETO / 'config'
ARQUIVO_CONFIG_RENAME_RULES = DIRETORIO_CONFIG / 'rename_rules.json'

caminho_criado = criar_estrutura_log(
    data_hora=datetime.now(),
    cultura='pt_BR',
    diretorio_base=DIRETORIO_PROJETO,
)

registar_log(
    log_level='DEBUG',
    mensagem=f'Iniciando a automação {NOME_AUTOMACAO}',
    cultura='pt_BR.UTF-8',
    handler_name='root',
)

with open(ARQUIVO_CONFIG_RENAME_RULES, encoding="utf-8") as arquivo_JSON:
    arquivo_config_rename_rules_json = load(arquivo_JSON)

# MOCK 
arquivo_config_rename_rules_json['diretorioEntrada'] = 'C:\\users\\aranseiki\\Downloads'
# FIM DO MOCK 

lista_arquivos = [
    item 
    for item in Path(
        arquivo_config_rename_rules_json['diretorioEntrada']
    ).glob('**/*.*')
    if item.is_file
]

