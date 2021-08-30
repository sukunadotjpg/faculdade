#cabeçalho #EXERCICIO 4
text = 'cadastrar produtos.py v1.0'
tam = len(text)
print('+','-' * tam,'+')
print('|',text,'|')
print('+','-' * tam,'+')

list = []

#funcao que adiciona os dicionarios na lista
def cad_prodt(cad: dict):
    list.append(cad)
    return

#coleta de dados e o chamado da funcao para adicionar os dict a list
while True:
    insert = int(input('deseja cadastrar produtos?\n0 - Não   1 - Sim\n'))
    if insert == True:
        produto = {}
        produto['codigo'] = int(input('insira o codigo do produto: ')) 
        produto['quantidade'] = int(input('insira a quantidade do produto: '))
        produto['minimo'] = int(input('insira a quantidade minima para o produto: '))
        cad_prodt(produto)
    else:           
        if len(list) > 0:
            print('a lista de produtos é:\n',list)
            break
        else:
            print('lista vazia\nencerrando o programa...')
            break
