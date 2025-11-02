# Módulo: consistencia.py
# Função: Responsável por salvar e carregar as tarefas de um arquivo JSON, garantindo a firmeza dos dados.

import json  # Biblioteca usada para manipular arquivos JSON
import os    # Usada para verificar se o arquivo já existe

# Nome do arquivo onde as tarefas serão armazenadas
ARQUIVO = "tarefas.json"

# Função que carrega as tarefas do arquivo JSON:
def carregar_tarefas():
    # Verifica se o arquivo já existe, se não existir, retorna uma lista vazia:
    if not os.path.exists(ARQUIVO):
        return []
    # Abre o arquivo em modo leitura e carrega os dados como lista:
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

# Função que salva as tarefas no arquivo JSON:
def salvar_tarefas(tarefas):
    # Abre o arquivo em modo escrita e salva a lista de tarefas formatada:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)