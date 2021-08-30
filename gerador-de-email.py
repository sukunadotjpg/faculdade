#cabecalho

text = 'gerador de email.py v2.0'
tam = len(text)
print('+','-' * tam,'+')
print('|',text,'|')
print('+','-' * tam,'+')

#funcao para entrada de dados e trabalhar com tuplas

def insert():
    nome = str(input('Digite o seu primeiro nome: '))
    sobrenome = str(input('Digite o seu nome e sobrenome: '))
    ru = str(input('Digite seu RU: '))
    print('o seu email é:', nome[0]+sobrenome+ru[5]+ru[6]+'@algoritimos.com.br'+'!')

insert()
