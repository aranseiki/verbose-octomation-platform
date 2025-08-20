import runpy

from system.config.config_file import DIRETORIO_RAIZ

print(__name__)

resultado_modulo = runpy.run_path(f'{DIRETORIO_RAIZ.parent}/../docs/exemplos/soma.py')
