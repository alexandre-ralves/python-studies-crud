# CRUD de Tarefas em Python

Este é um projeto de estudo que implementa um **CRUD (Create, Read, Update, Delete)** de tarefas usando **Python puro**, com dados armazenados em um arquivo JSON e testes automatizados com `pytest`.

O projeto foi desenvolvido com **boas práticas de organização**, como separação de responsabilidades em módulos, ambiente virtual isolado e tasks de automação no VS Code.

---

## 📁 Estrutura do Projeto

```
crud_python/
│
├── app/
│   ├── main.py          ← Menu principal e entrada do programa
│   ├── tarefas.py       ← Lógica de criação, leitura, atualização e exclusão de tarefas
│   └── utils.py         ← Funções auxiliares (carregar/salvar tarefas)
│
├── data/
│   └── db.json          ← "Banco de dados" local em formato JSON
│
├── tests/
│   └── test_tarefas.py  ← Testes automatizados com pytest
│
├── .vscode/
│   └── tasks.json       ← Task runner configurado para rodar testes no VS Code
│
├── .venv/               ← Ambiente virtual (não enviado para o GitHub)
│
├── pytest.ini           ← Configuração do pytest
├── requirements.txt     ← Dependências do projeto
└── README.md            ← Documentação do projeto
```

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/alexandre-ralves/python-studies-crud.git
cd python-studies-crud
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python3 -m app.main
```

---

## Como rodar os testes

### Usando o terminal

```bash
PYTHONPATH=. pytest
```

### Usando Task no VS Code

1. Abra o projeto no VS Code.
2. Aperte `Cmd+Shift+P` → "Run Task"
3. Escolha a task `Rodar Testes`
4. Seus testes serão executados automaticamente no terminal integrado.

---

## Funcionalidades do projeto

- ✅ Criar novas tarefas
- ✅ Listar todas as tarefas (mostrando status de conclusão)
- ✅ Marcar tarefas como concluídas
- ✅ Excluir tarefas existentes
- ✅ Uso de `UUID` para identificar tarefas de forma única
- ✅ Ambiente isolado com `.venv`
- ✅ Testes automatizados de criação, leitura, atualização e exclusão de tarefas
- ✅ Configuração de Task Runner para rodar testes no VS Code

---

## Tecnologias e ferramentas usadas

- **Python 3.9+**
- **pytest** (para testes automatizados)
- **VS Code** (com configuração de tasks)
- **JSON** (para persistência de dados)
- **UUID** (para IDs únicos nas tarefas)

---

## 📌 Melhorias futuras

- Implementar edição do título de tarefas
- Organizar tarefas por status (pendente/concluída)
- Persistência dos dados usando banco de dados real
- Automatizar execução de testes com GitHub Actions no pipeline de CI

---

## ✨ Autor

- **Alexandre Alves**
- GitHub: [@alexandre-ralves](https://github.com/alexandre-ralves)

---
