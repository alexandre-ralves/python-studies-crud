import json
import os
import sqlite3

def carregar_tarefas(db_file="data/db.json"):
    if not os.path.exists(db_file):
        return []
    with open(db_file, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas, db_file="data/db.json"):
    with open(db_file, "w") as f:
        json.dump(tarefas, f, indent=4)

# Criação do banco de dados SQLite e da tabela de tarefas

def init_db(db_path="data/tarefas.db"):
    # Garante que a pasta 'data/' exista
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Conecta (ou cria) o banco
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    # Cria a tabela de tarefas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        concluida BOOLEAN NOT NULL
    )
    ''')

    conexao.commit()
    conexao.close()

    print("✅ Banco de dados inicializado!")
