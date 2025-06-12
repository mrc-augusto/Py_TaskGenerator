def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {'tarefa': nome_tarefa, 'completa': False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} foi adicionada com sucesso!') 
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa foi adicionada.')
        return

    elif tarefas:
        print('\nLista de Tarefas: ')
        for indice, tarefa, in enumerate(tarefas, start=1):
            status = '✔' if tarefa['completa'] else 'Pendente '
            nome_tarefa = tarefa['tarefa']
            print(f'{indice}. [{status}] {nome_tarefa}')
            
1
tarefas = []

while True:
    print('\nMenu do Gerenciador de Tarefas: ')
    print('1. Adicionar Tarefa ')
    print('2. Ver Tarefas')
    print('3. Atualizar Tarefa')
    print('4. Completar Tarefa')
    print('5. Deletar Tarefas Completadas')
    print('6. Sair ')

    escolha = input('Digite a sua escolha:')

    if escolha == '1':
        nome_tarefa = input('Digite o nome da tarefa:')
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == '2':
        ver_tarefas(tarefas)

    elif escolha == '6':
        break
    
print('Programa Finalizado')
