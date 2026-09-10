import json
import f
lista_tarefas = []
while True:
    print("1 - Cadastrar tarefa")
    print("2 - Atualizar tarefa")
    print("3 - Ver tarefas")
    print("4 - Sair")
    opc = int(input("Digite a opção desejada: "))
    if opc == 1:
        lista_tarefas.append(f.cadastrar_tarefa(lista_tarefas))
    elif opc == 2:
        lista_tarefas = f.atualizar_tarefa(lista_tarefas)
    elif opc == 3:
        lista_tarefas = f.resumo_tarefas(lista_tarefas)
    elif opc == 4:
        print("Saindo do programa...")
        break
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo, default=str)
    print("Tarefas salvas em tarefas.json")