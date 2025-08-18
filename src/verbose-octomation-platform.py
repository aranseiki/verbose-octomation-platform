import runpy

from config.config import DIRETORIO_RAIZ

print(__name__)

resultado_modulo = runpy.run_path(
    f'{DIRETORIO_RAIZ.parent}/src/soma.py'
)
