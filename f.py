import datetime
import json

lista_tarefas = []
def cadastrar_tarefa():
    tarefa={}
    nome=input("Digite o nome da tarefa: ")
    descricao=input("Digite a descrição da tarefa: ")
    tarefa={
        'id': len(lista_tarefas)+1,
        'nome': nome,
        'descricao': descricao,
        'data_criado': datetime.datetime.now(),
        'data_atualizacao': datetime.datetime.now(),
        'status': 'Andamento'
    }
    lista_tarefas.append(tarefa.copy())
    print(lista_tarefas)

def atualizar_tarefa():
   opc=int(input("Digite o id da tarefa que deseja atualizar: "))
   for t in lista_tarefas:
        if t['id'] == opc:
            t['nome'] = input("Digite o novo nome da tarefa: ")
            t['descricao'] = input("Digite a nova descrição da tarefa: ")
            t['data_atualizacao'] = datetime.datetime.now()
            t['status'] = input("Digite o novo status da tarefa: ")
            print("Tarefa atualizada com sucesso!")
            return lista_tarefas

def resumo_tarefas():
    print("Resumo das tarefas:")
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for t in lista_tarefas:
            print(f"ID: {t['id']}")
            print(f"Nome: {t['nome']}")
            print(f"Descrição: {t['descricao']}")
            print(f"Data de criação: {t['data_criado']}")
            print(f"Data de atualização: {t['data_atualizacao']}")
            print(f"Status: {t['status']}")
            print("-" * 30)

def menu():
    while True:
        print("1 - Cadastrar tarefa")
        print("2 - Atualizar tarefa")
        print("3 - Ver tarefas")
        print("4 - Sair")
        opc = int(input("Digite a opção desejada: "))
        if opc == 1:
            cadastrar_tarefa()
        elif opc == 2:
            atualizar_tarefa()
        elif opc == 3:
            resumo_tarefas()
        elif opc == 4:
            print("Saindo do programa...")
            break
        with open("tarefas.json", "w") as arquivo:
                json.dump(lista_tarefas, arquivo, default=str)
        print("Tarefas salvas em tarefas.json")