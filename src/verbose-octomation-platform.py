import runpy
import threading
import time
from pathlib import Path

import docker

from system.config.config_file import DIRETORIO_RAIZ

# breakpoint()

AUTOMACOES = {
    'soma': Path('docs/exemplos/soma.py'),
    'renomear_arquivos_em_lote': Path(
        f'{DIRETORIO_RAIZ}/RPA/renomear_arquivos_em_lote/renomear_arquivos_em_lote.py'
    ),
    # Adicione outras automações aqui
}

INSTANCIAS_ATIVAS = {}


def executar_automacao(nome):
    caminho = AUTOMACOES.get(nome)
    if not caminho:
        print(f"Automação '{nome}' não encontrada.")
        return
    print(f'Executando: {nome}')
    resultado_modulo = runpy.run_path(str(caminho))
    print(f'Resultado: {resultado_modulo}')


def agendar_automacao(nome, delay_segundos):
    thread = threading.Timer(delay_segundos, executar_automacao, args=(nome,))
    INSTANCIAS_ATIVAS[nome] = thread


def iniciar_automacao(thread):
    thread.start()


def listar_automacoes():
    print('Automações disponíveis:')
    for nome in AUTOMACOES:
        print(f'- {nome}')


def executar_automacao_docker(nome):
    client = docker.from_env()
    image = f'meu_repo/{nome}:latest'
    try:
        container = client.containers.run(image, detach=True)
        print(f'Container {container.short_id} iniciado para {nome}')
    except Exception as e:
        print(f'Erro ao iniciar container: {e}')


if __name__ == '__main__':
    listar_automacoes()
    agendar_automacao('soma', 5)  # Exemplo: agenda para daqui 5 segundos
    agendar_automacao(
        'renomear_arquivos_em_lote', 5
    )  # Exemplo: agenda para daqui 5 segundos
    # breakpoint()
    for thread in INSTANCIAS_ATIVAS:
        iniciar_automacao(INSTANCIAS_ATIVAS[thread])
        # executar_automacao_docker(thread)

    while any(t.is_alive() for t in INSTANCIAS_ATIVAS.values()):
        time.sleep(1)

    print('Todas as automações agendadas finalizaram.')
