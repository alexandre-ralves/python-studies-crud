from app.tarefas import criar_tarefa, listar_tarefas, concluir_tarefa, excluir_tarefa
from app.utils import carregar_tarefas, salvar_tarefas
import pytest
import uuid

# Função auxiliar para simular input

def input_simulado(valor):
    def inner_input(mensagem=""):
        return valor
    return inner_input

# Testes de criação de tarefas

def test_criar_tarefa(tmp_path):
    db_fake = tmp_path / "db.json"
    salvar_tarefas([], db_file=db_fake)

    criar_tarefa(input_fn=input_simulado("Estudar Python"), db_file=db_fake)

    tarefas = carregar_tarefas(db_file=db_fake)
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"
    assert tarefas[0]["concluida"] is False


# Testes de listagem de tarefas

def test_listar_tarefas_vazias(capsys, tmp_path):
    db_fake = tmp_path / "db.json"
    salvar_tarefas([], db_file=db_fake)

    listar_tarefas(db_file=db_fake)

    captured = capsys.readouterr()
    assert "Nenhuma tarefa encontrada." in captured.out

def test_listar_tarefas_existentes(capsys, tmp_path):
    db_fake = tmp_path / "db.json"
    tarefas_exemplo = [
        {"id": "123", "titulo": "Tarefa Exemplo", "concluida": False}
    ]
    salvar_tarefas(tarefas_exemplo, db_file=db_fake)

    listar_tarefas(db_file=db_fake)

    captured = capsys.readouterr()
    assert "Tarefa Exemplo" in captured.out


# Testes de conclusão de tarefas

def test_concluir_tarefa(tmp_path):
    db_fake = tmp_path / "db.json"
    tarefas_exemplo = [
        {"id": "123", "titulo": "Tarefa a concluir", "concluida": False}
    ]
    salvar_tarefas(tarefas_exemplo, db_file=db_fake)

    concluir_tarefa(input_fn=input_simulado("123"), db_file=db_fake)

    tarefas = carregar_tarefas(db_file=db_fake)
    assert tarefas[0]["concluida"] is True


# Testes de exclusão de tarefas

def test_excluir_tarefa(tmp_path):
    db_fake = tmp_path / "db.json"
    tarefas_exemplo = [
        {"id": "123", "titulo": "Tarefa a excluir", "concluida": False}
    ]
    salvar_tarefas(tarefas_exemplo, db_file=db_fake)

    excluir_tarefa(input_fn=input_simulado("123"), db_file=db_fake)

    tarefas = carregar_tarefas(db_file=db_fake)
    assert len(tarefas) == 0
