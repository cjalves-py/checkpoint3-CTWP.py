# Módulo: tarefas.py
# Função: Contém as funções principais do sistema que são cadastrar, listar, atualizar e remover tarefas.

# Para lidar com datas
from datetime import datetime

# Importa funções do módulo de consistência
from consistencia import carregar_tarefas, salvar_tarefas


# Função: cadastrar_tarefa()
# Cadastra uma nova tarefa com descrição, data e status inicial.
def cadastrar_tarefa(descricao, data_vencimento, status="pendente", prioridade="média"):
    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "data_vencimento": data_vencimento,
        "status": status,
        #campo prioridade
        "prioridade": prioridade
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa cadastrada com sucesso!")

# Função: listar_tarefas()
# Lista todas as tarefas cadastradas, podendo filtrar por status.

def listar_tarefas(filtro_status=None):
    tarefas = carregar_tarefas()
    if filtro_status:
        tarefas = [t for t in tarefas if t["status"] == filtro_status]

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n Lista de Tarefas:")
    for t in tarefas:
        print(f"ID: {t['id']} | Descrição: {t['descricao']} | "
              f"Vencimento: {t['data_vencimento']} | "
              f"Status: {t['status']} | "
              f"Prioridade: {t['prioridade']}")
        

# Função: atualizar_tarefa()
# Atualiza a descrição, data ou status de uma tarefa existente.

def atualizar_tarefa(id_tarefa, nova_descricao=None, nova_data=None, novo_status=None, nova_prioridade=None):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id_tarefa:
            if nova_descricao:
                t["descricao"] = nova_descricao
            if nova_data:
                t["data_vencimento"] = nova_data
            if novo_status:
                t["status"] = novo_status
            if nova_prioridade:
                t["prioridade"] = nova_prioridade
            salvar_tarefas(tarefas)
            print("Tarefa atualizada com sucesso!")
            return
    print("Tarefa não encontrada.")


# Função: remover_tarefa()
# Permite também editar a prioridade de uma tarefa.

def remover_tarefa(id_tarefa):
    tarefas = carregar_tarefas()
    # Cria uma nova lista sem a tarefa que deve ser removida
    novas_tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    if len(novas_tarefas) != len(tarefas):
        salvar_tarefas(novas_tarefas)
        print("Tarefa removida com sucesso!")
    else:
        print("Tarefa não encontrada.")
