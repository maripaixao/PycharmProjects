from random import randint
from time import sleep
print('\033[34m-=\033[m' * 8)
print('\033[33m J O K E N P O \033[m')
print('\033[34m-=\033[m' * 8)
itens = ['Pedra', 'Papel', 'Tesoura']
print('0 - PEDRA')
print('1 - PAPEL')
print('2 - TESOURA')
jogador = int(input('Faça a sua jogada: '))
comp = randint(0, 2)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 10)
print(f'Jogador: {itens[jogador]}')
print(f'Computador: {itens[comp]}')
print('-=' * 10)
if jogador == comp:
    print('EMPATE!!')
elif jogador == 0 and comp == 2 or jogador == 2 and comp == 0:
    if jogador == 0:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    else:
        print('\033[31mVOCÊ PERDEU! :(\033[m')
    print('Pedra ganha da Tesoura!')
elif jogador == 0 and comp == 1 or jogador == 1 and comp == 0:
    if jogador == 1:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    else:
        print('\033[31mVOCÊ PERDEU! :(\033[m')
    print('Papel ganha da Pedra')
elif jogador == 2 and comp == 1 or jogador == 1 and comp == 2:
    if jogador == 2:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    else:
        print('\033[31mVOCÊ PERDEU! :(\033[m')
    print('Tesoura ganha do Papel')