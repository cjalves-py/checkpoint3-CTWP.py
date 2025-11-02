# Módulo: interface.py
# Função: Cria a interface de linha de comando para interação com o usuário (menu principal).


from tarefas import cadastrar_tarefa, listar_tarefas, atualizar_tarefa, remover_tarefa

# Função: menu()
# Exibe o menu principal e direciona o usuário para a função que o mesmo escolheu.

def menu():
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Cadastrar nova tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar tarefa")
        print("4. Remover tarefa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        # Cadastrar nova tarefa:
        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            data = input("Data de vencimento (AAAA-MM-DD): ")
            prioridade = input("Prioridade (baixa/média/alta): ") or "média"
            cadastrar_tarefa(descricao, data, prioridade=prioridade)

        # Listar tarefas:
        elif opcao == "2":
            filtro = input("Filtrar por status (pendente/andamento/concluída ou Enter p/ todos): ").strip()
            filtro = filtro if filtro else None
            listar_tarefas(filtro)

        # Atualizar tarefa:
        elif opcao == "3":
            id_tarefa = int(input("ID da tarefa a atualizar: "))
            nova_desc = input("Nova descrição (ou Enter p/ manter): ") or None
            nova_data = input("Nova data (ou Enter p/ manter): ") or None
            novo_status = input("Novo status (pendente/andamento/concluída ou Enter p/ manter): ") or None
            nova_prioridade = input("Nova prioridade (baixa/média/alta ou Enter p/ manter): ") or None
            atualizar_tarefa(id_tarefa, nova_desc, nova_data, novo_status, nova_prioridade)

        # Remover tarefa:
        elif opcao == "4":
            id_tarefa = int(input("ID da tarefa a remover: "))
            remover_tarefa(id_tarefa)

        # Encerrar o programa:
        elif opcao == "0":
            print("Saindo... Até logo!")
            break

        # Opção inválida:
        else:
            print("Opção inválida, tente novamente.")