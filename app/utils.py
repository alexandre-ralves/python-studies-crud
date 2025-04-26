import json
import os

def carregar_tarefas(db_file="data/db.json"):
    if not os.path.exists(db_file):
        return []
    with open(db_file, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas, db_file="data/db.json"):
    with open(db_file, "w") as f:
        json.dump(tarefas, f, indent=4)
