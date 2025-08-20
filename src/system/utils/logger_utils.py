import sys
import os

# garante que src esteja no sys.path mesmo quando executado diretamente
CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from system.config.config_file import DIRETORIO_RAIZ

import logging
import logging.config
from datetime import datetime
from functools import wraps


def localizar_data_hora(
    datetime: datetime,
    cultura: str,
):
    import locale

    locale.setlocale(locale.LC_TIME, cultura)
    data_hora_atual = datetime
    return data_hora_atual.strftime('%c')


def definir_log_config(
    log_level: str,
    cultura: str,
    handler_name: str,
    arquivo_config: str,
):
    if not isinstance(handler_name, str):
        raise ValueError('Você precisa definir um Handler para o log.')

    LEVELNAMESMAPPING = list(logging.getLevelNamesMapping().keys())
    if not log_level in LEVELNAMESMAPPING:
        raise ValueError(
            'Você precisa definir um '
            f'dos seguintes níveis: {LEVELNAMESMAPPING}.'
        )

    logging.config.fileConfig(arquivo_config)
    logger = logging.getLogger(handler_name)
    if log_level.upper() == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
        logging_with_level = logger.critical
    elif log_level.upper() == 'FATAL':
        logger.setLevel(logging.FATAL)
        logging_with_level = logger.fatal
    elif log_level.upper() == 'ERROR':
        logger.setLevel(logging.ERROR)
        logging_with_level = logger.error
    elif (log_level.upper() == 'WARN') or (log_level.upper() == 'WARNING'):
        logger.setLevel(logging.WARNING)
        logging_with_level = logger.warning
    elif log_level.upper() == 'INFO':
        logger.setLevel(logging.INFO)
        logging_with_level = logger.info
    elif log_level.upper() == 'DEBUG':
        logger.setLevel(logging.DEBUG)
        logging_with_level = logger.debug
    elif log_level.upper() == 'NOTSET':
        logger.setLevel(logging.NOTSET)

        def logging_with_level(msg, **kwargs):
            logger.log(logging.NOTSET, msg, **kwargs)

    else:
        raise ValueError('Nìvel não mapeado.')

    data_hora_atual = localizar_data_hora(
        datetime=datetime.now(), cultura=cultura
    )
    extra_log_config = {'data_hora_atual': data_hora_atual}

    return logging_with_level, extra_log_config


def registar_log(
    log_level: str,
    mensagem: str,
    cultura: str,
    handler_name: str,
    arquivo_config: str = f'{DIRETORIO_RAIZ}/logging.ini',
):
    try:
        erro_logging = None
        logging_with_level = None
        extra = {}

        logging_with_level, extra = definir_log_config(
            log_level,
            cultura,
            handler_name,
            arquivo_config,
        )
        logging_with_level(msg=mensagem, extra=extra)
    except Exception as erro_logging:
        if (not logging_with_level) or (not extra):
            raise LookupError(
                'Um erro aconteceu na configuração do log'
            ) from erro_logging

        logging_with_level(msg=str(erro_logging), extra=extra)
    finally:
        if erro_logging is not None:
            raise erro_logging


def registar_log_decorator(
    log_level: str,
    mensagem: str,
    cultura: str,
    handler_name: str,
    arquivo_config: str = f'{DIRETORIO_RAIZ}/logging.ini',
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            registar_log(
                log_level, mensagem, cultura, handler_name, arquivo_config
            )
            resultado = func(*args, **kwargs)

            return resultado

        return wrapper

    return decorator
