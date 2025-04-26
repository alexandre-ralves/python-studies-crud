import uuid
from app.utils import carregar_tarefas, salvar_tarefas

def criar_tarefa(input_fn=input, db_file="data/db.json"):
    titulo = input_fn("Digite o título da tarefa: ")
    nova_tarefa = {
        "id": str(uuid.uuid4()),
        "titulo": titulo,
        "concluida": False
    }

    tarefas = carregar_tarefas(db_file=db_file)
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas, db_file=db_file)

    print("Tarefa criada com sucesso!")

def listar_tarefas(db_file="data/db.json"):
    tarefas = carregar_tarefas(db_file=db_file)

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n=== Tarefas ===")
    for tarefa in tarefas:
        status = "✅" if tarefa["concluida"] else "❌"
        print(f'{tarefa["id"]} - {tarefa["titulo"]} [{status}]')

def concluir_tarefa(input_fn=input, db_file="data/db.json"):
    tarefas = carregar_tarefas(db_file=db_file)

    if not tarefas:
        print("Nenhuma tarefa para concluir.")
        return

    listar_tarefas(db_file=db_file)

    id_escolhido = input_fn("Digite o ID da tarefa que deseja concluir: ")

    for tarefa in tarefas:
        if tarefa["id"] == id_escolhido:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas, db_file=db_file)
            print("Tarefa marcada como concluída! ✅")
            return

    print("Tarefa com esse ID não encontrada.")

def excluir_tarefa(input_fn=input, db_file="data/db.json"):
    tarefas = carregar_tarefas(db_file=db_file)

    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return

    listar_tarefas(db_file=db_file)

    id_escolhido = input_fn("Digite o ID da tarefa que deseja excluir: ")

    nova_lista = [tarefa for tarefa in tarefas if tarefa["id"] != id_escolhido]

    if len(nova_lista) == len(tarefas):
        print("Tarefa com esse ID não encontrada.")
    else:
        salvar_tarefas(nova_lista, db_file=db_file)
        print("Tarefa excluída com sucesso! 🗑️")