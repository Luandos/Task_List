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
        'data_criado': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        'data_atualizacao': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        'status': 'Andamento'
    }
    lista_tarefas.append(tarefa.copy())
    print(lista_tarefas)

def atualizar_tarefa():
    try:
      opc=int(input("Digite o id da tarefa que deseja atualizar: "))
      if opc < 1 or opc > len(lista_tarefas):
        raise ValueError("Opção inválida. Por favor, digite um número válido.")
    except ValueError as e:
        print(f"Opção inválida. Por favor, digite um número. Error: {e}")
        return
    for t in lista_tarefas:
        if t['id'] == opc:
            pergunta=input("Deseja atualizar somente o status? (s/n): ").strip().lower()
            if pergunta == 's':
                t['status'] = input("Digite o novo status da tarefa: ")
            else:
                t['nome'] = input("Digite o novo nome da tarefa: ")
                t['descricao'] = input("Digite a nova descrição da tarefa: ")
                t['data_atualizacao'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
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
    try:
        pergunta=input("Deseja ver apenas as tarefas pendentes? (s/n): ").strip().lower()
        if pergunta not in ['s', 'n']:
            raise ValueError("Opção inválida. Por favor, digite 's' ou 'n'.")
    except Exception as error:
        print(f"Error: {error}")
    if pergunta == 's':
        print("Tarefas pendentes:")
        for t in lista_tarefas:
            if t['status'] == 'Andamento':
                print(f"ID: {t['id']}")
                print(f"Nome: {t['nome']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Data de criação: {t['data_criado']}")
                print(f"Data de atualização: {t['data_atualizacao']}")
                print(f"Status: {t['status']}")
                print("-" * 30)
    try:
        pergunta=input("Deseja ver apenas as tarefas concluídas? (s/n): ").strip().lower()
        if pergunta not in ['s', 'n']:
            raise ValueError("Opção inválida. Por favor, digite 's' ou 'n'.")
    except Exception as error:
            print(f"Error: {error}")
    if pergunta == 's':
        print("Tarefas concluídas:")
        for t in lista_tarefas:
            if t['status'] == 'Concluída':
                print(f"ID: {t['id']}")
                print(f"Nome: {t['nome']}")
                print(f"Descrição: {t['descricao']}")
                print(f"Data de criação: {t['data_criado']}")
                print(f"Data de atualização: {t['data_atualizacao']}")
                print(f"Status: {t['status']}")
                print("-" * 30)

def excluir_tarefa():
    try:
        opc=int(input("Digite o id da tarefa que deseja excluir: "))
        if opc < 1 or opc > len(lista_tarefas):
            raise ValueError("Opção inválida. Por favor, digite um número válido.")
    except ValueError as e:
        print(f"Opção inválida. Por favor, digite um número. Error: {e}")
        return
    for t in lista_tarefas:
        if t['id'] == opc:
            lista_tarefas.remove(t)
            print("Tarefa excluída com sucesso!")
            return lista_tarefas
    print("Tarefa não encontrada.")

def menu():
    while True:
        print("1 - Cadastrar tarefa")
        print("2 - Atualizar tarefa")
        print("3 - Ver tarefas")
        print("4 - Excluir tarefa")
        print("5 - Sair")
        try:
            opc = int(input("Digite a opção desejada: "))
            if opc < 1 or opc > 5:
                raise ValueError("Opção inválida. Por favor, digite um número entre 1 e 5.")
        except Exception as e:
            print(f"Opção inválida. Por favor, digite um número. Error: {e}")
            return
        if opc == 1:
            cadastrar_tarefa()
        elif opc == 2:
            atualizar_tarefa()
        elif opc == 3:
            resumo_tarefas()
        elif opc == 4:
            excluir_tarefa()
        elif opc == 5:
            print("Saindo do programa...")
            break
        with open("tarefas.json", "w") as arquivo:
                json.dump(lista_tarefas, arquivo, default=str)
        print("Tarefas salvas em tarefas.json")