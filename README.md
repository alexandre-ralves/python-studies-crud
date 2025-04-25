# CRUD de Tarefas em Python

Este é um projeto simples de **CRUD (Create, Read, Update, Delete)** feito em **Python puro**, utilizando arquivos JSON para salvar as tarefas — sem banco de dados ou bibliotecas externas.

---

## Estrutura do Projeto

```
crud_python/
│
├── app/
│   ├── main.py           ← Código principal responsável pela navegação e controle das demais funções
|   ├── tarefas.py        ← Funções de gerenciamento das tarefas: criação, edição/movimentação de status, e exclusão.
|   ├── utils.py          ← Funções de leitura e gravação das tarefas.
│
├── data/
│   └── db.json           ← "Banco de dados" simulado com um arquivo em formato JSON.
│
└── README.md             ← Este arquivo.
```

---

## Como executar

1. Certifique-se de que o Python 3 está instalado:

```bash
python3 --version
```

2. No terminal, entre na pasta do projeto:

```bash
cd crud_python
```

3. Execute o programa:

```bash
python3 -m app/main.py
```

---

## Funcionalidades

No terminal, você verá este menu:

```
=== Lista de Tarefas ===
1 - Criar nova tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Excluir tarefa
0 - Sair
```

- **1 - Criar**: Adiciona uma nova tarefa com título
- **2 - Listar**: Exibe todas as tarefas salvas
- **3 - Concluir**: Marca uma tarefa como feita
- **4 - Excluir**: Remove uma tarefa do sistema
- **0 - Sair**: Encerra o programa

---

## Tecnologias utilizadas

- Python 3
- Módulos padrão: `json`, `os`
