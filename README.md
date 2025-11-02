# Gerenciador de Tarefas (Python)

Um projeto simples de sistema de gerenciamento de tarefas, feito em Python, que roda direto no terminal.
A ideia é permitir cadastrar, listar, atualizar e remover tarefas — tudo salvo em arquivo, pra não perder nada quando o programa fecha.

# O que dá pra fazer

O sistema tem as seguintes funcionalidades:

- Cadastrar tarefas com descrição, data de vencimento, prioridade (baixa, média ou alta) e status (pendente, em andamento ou concluída);

- Listar tarefas podendo filtrar por status e visualizar a prioridade de cada uma;

- Atualizar tarefas permitindo editar descrição, data, status e prioridade;

- Remover tarefas já concluídas ou que não são mais necessárias;

- Salvar tudo em arquivo JSON, garantindo que as informações fiquem guardadas.

# Estrutura do Projeto

O projeto foi dividido em módulos pra deixar o código mais organizado e eficiente:

gerenciador_tarefas:

│
|--tarefas.py         # Funções principais: criar, listar, atualizar e remover tarefas;
|-- persistencia.py   # Responsável por salvar e carregar as tarefas do arquivo JSON;
|--interface.py       # Interface de linha de comando (menu);
|--main.py            # Arquivo principal que roda o programa.

# Como Rodar o Projeto

Antes de tudo, garanta que você tem o Python 3 instalado.
Você pode verificar isso no terminal com:

python --version


ou (dependendo do sistema):

python3 --version

- Passo a passo pra rodar

- Baixe ou clone o projeto

Se estiver no VS Code, pode simplesmente criar uma pasta chamada gerenciador_tarefas e colocar os arquivos lá.

- Abra o terminal dentro da pasta do projeto.

- Execute o programa:

python main.py


(ou python3 main.py, se o seu sistema usar esse comando)

Pronto!
Vai aparecer um menu com as opções:

1. Cadastrar nova tarefa
2. Listar tarefas
3. Atualizar tarefa
4. Remover tarefa
0. Sair

# Como funciona por trás

As tarefas são armazenadas em um arquivo chamado tarefas.json.

Cada tarefa tem:

{
  "id": 1,
  "descricao": "Estudar Python",
  "data_vencimento": "2025-11-10",
  "status": "pendente"
}


O programa lê e atualiza esse arquivo automaticamente a cada ação (cadastrar, editar ou remover).

# Dicas

Use datas no formato AAAA-MM-DD (exemplo: 2025-11-02);

Cada tarefa tem os seguintes campos:
- id - número de identificação
- descricao - o que deve ser feito
- data_vencimento - prazo da tarefa (AAAA-MM-DD)
- status - pendente, andamento ou concluída
- prioridade - baixa, média ou alta.

# Alunos que desenvolveram o projeto

Claudio Alves - RM 568565

Luna Rousseau - RM 564215

Rodrigo G. Wolk - RM 556980
