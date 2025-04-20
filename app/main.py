import json
import os

DB_FILE = "data/db.json"

def carregar_tarefas():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(DB_FILE, "w") as f:
        json.dump(tarefas, f, indent=4)

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    nova_tarefa = {
        "id": gerar_id(),
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
        id_escolhido = int(input("Digite o ID da tarefa que deseja concluir: "))
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

def gerar_id():
    tarefas = carregar_tarefas()
    if not tarefas:
        return 1
    else:
        ultimo_id = tarefas[-1]["id"]
        return ultimo_id + 1

def main():
    while True:
        print("\n=== Lista de Tarefas ===")
        print("1 - Criar nova tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "0":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
