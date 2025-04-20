import uuid
from app.utils import carregar_tarefas, salvar_tarefas

DB_FILE = "data/db.json"

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    nova_tarefa = {
        "id": str(uuid.uuid4()),
        "titulo": titulo,
        "concluida": False
    }

    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa criada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n=== Tarefas ===")
    for tarefa in tarefas:
        status = "✅" if tarefa["concluida"] else "❌"
        print(f'{tarefa["id"]} - {tarefa["titulo"]} [{status}]')

def concluir_tarefa():
    tarefas = carregar_tarefas()
    
    if not tarefas:
        print("Nenhuma tarefa para concluir.")
        return

    listar_tarefas()

    try:
        id_escolhido = input("Digite o ID da tarefa que deseja concluir: ")
    except ValueError:
        print("ID inválido.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_escolhido:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída! ✅")
            return

    print("Tarefa com esse ID não encontrada.")

def excluir_tarefa():
    tarefas = carregar_tarefas()

    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return

    listar_tarefas()

    try:
        id_escolhido = int(input("Digite o ID da tarefa que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    nova_lista = [tarefa for tarefa in tarefas if tarefa["id"] != id_escolhido]

    if len(nova_lista) == len(tarefas):
        print("Tarefa com esse ID não encontrada.")
    else:
        salvar_tarefas(nova_lista)
        print("Tarefa excluída com sucesso! 🗑️")