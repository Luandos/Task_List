import datetime
def cadastrar_tarefa(lista):
    tarefa={}
    tarefa['nome'] = input("Digite o nome da tarefa: ")
    tarefa['descricao'] = input("Digite a descrição da tarefa: ")
    tarefa['data_criado'] = datetime.datetime.now()
    tarefa['data_atualizacao'] = datetime.datetime.now()
    tarefa['status'] = 'Andamento'
    tarefa['id'] = len(lista) + 1
    print(tarefa.values())
    return tarefa

def atualizar_tarefa(list):
   opc=int(input("Digite o id da tarefa que deseja atualizar: "))
   for lista in enumerate(list):
       for t in lista:
            if t['id'] == opc:
                t['nome'] = input("Digite o novo nome da tarefa: ")
                t['descricao'] = input("Digite a nova descrição da tarefa: ")
                t['data_atualizacao'] = datetime.datetime.now()
                t['status'] = input("Digite o novo status da tarefa: ")
                print("Tarefa atualizada com sucesso!")
                return list

def resumo_tarefas(lista):
    for l in enumerate(lista):
        for tarefa in l:
            print(f"ID: {tarefa['id']}")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Data de criação: {tarefa['data_criado']}")
            print(f"Data de atualização: {tarefa['data_atualizacao']}")
            print(f"Status: {tarefa['status']}")
            print("--------------------")