# Lista de Preços com Tuplas
listagem = ('Mousepad', 30,
            'Notebook Gamer', 4899,
            'Cadeira', 749.90,
            'Mouse', 49.83,
            'Headset', 299.90,
            'Mesa p/ Computador', 599)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-' * 40)