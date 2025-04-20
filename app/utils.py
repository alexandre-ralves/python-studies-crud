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
