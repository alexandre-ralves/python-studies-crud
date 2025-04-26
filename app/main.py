from app.tarefas import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)
from app.utils import init_db

def main():
    init_db()  # ← inicializa o banco de dados aqui
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
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
