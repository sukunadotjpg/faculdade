#cabeçalho #EXERCICIO 1
text = 'programa para leitura de notas beta teste v1.0'
tam = len(text)
print('+','-' * tam,'+')
print('|',text,'|')
print('+','-' * tam,'+')

#função para a entrada de dados
def entrada():
    global nota, nome
    print('PREENCHA O FORMULÁRIO PARA RECEBER OS RESULTADOS.')
    nome = str(input('nome do aluno: '))
    nota = float(input('nota do aluno: '))
    return nota, nome

#função do resultado
def resultado():
    if nota >= 0.0 and nota <= 2.9:
        print('{} tirou a nota {} que se enquadra na categoria E' .format(nome, nota))
    elif nota >= 3.0 and nota <= 4.9:
        print('{} tirou a nota {} que se enquadra na categoria D' .format(nome, nota))
    elif nota >= 5.0 and nota <= 6.9:
        print('{} tirou a nota {} que se enquadra na categoria C' .format(nome, nota))
    elif nota >= 7.0 and nota <= 8.9:
        print('{} tirou a nota {} que se enquadra na categoria B' .format(nome, nota))
    elif nota >= 9.0 and nota <= 10.0:
        print('{} tiroy a nota {} que se enquadra na categoria A' .format(nome, nota))
    else:
        print('Oops! Infelizmente ocorreu um erro inesperado. Tente novamente.')

#laço para o funcionamento do algoritmo
while True:
    insert = int(input('deseja inserir dados?\n0 - Não    1 - Sim\n'))
    if insert == True:
        entrada()
        resultado()
    else:
        print('encerrando o programa...')
        break

