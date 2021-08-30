import random

#cabecalho
text = 'algoritmo para sorteio beta alpha test v1.0'
tam = len(text)
print('+','-' * tam,'+')
print('|',text,'|')
print('+','-' * tam,'+')

#funcao para adicionar dados na lista
lista_doadores = []
def dados(doadores, valor):
    lista_doadores.extend(((doadores+' ') * int(valor//10)).split())
    return

#funcao sorteio
def sorteio():
    random.shuffle(lista_doadores)
    sorteado = random.choice(lista_doadores)
    print(sorteado)

#laço e entrada de dados
while True:
    insert = int(input('deseja cadastrar os doadores?  \n0 - Não  1 - Sim\n'))
    if insert == True:
        nome = str(input('insira o nome do doador: '))
        doacao = float(input('insira a quantidade doada: '))
        while doacao == 0 or doacao < 10:
            print('o valor mínimo da doação para o sorteio é de 10 reais!')
            nome = str(input('insira o nome do doador: '))
            doacao = float(input('insira a quantidade doada: '))
        
        dados(nome, doacao)
    
    else:
        print('a lista de doadores é:', lista_doadores)
        print('o sorteado foi...')
        sorteio()
        break
