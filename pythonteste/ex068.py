# Jogo do Par ou Impar
from random import randint
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)
num = s = c = 0
pi = ''
while True:
    num = int(input('Diga um valor: '))
    pi = str(input('Par ou Impar? [P/I] ')).upper()
    pc = randint(0, 10)
    print('-=' * 20)
    s = pc + num
    c += 1
    print(f'Você jogou {num} e o computador {pc}. Total {s}. DEU ', end='')
    if s % 2 == 0 and pi in 'Pp' or s % 2 == 0 and pi in 'Pp':
        print('PAR')
        print('-' * 40)
        print('VOCÊ VENCEU')
        print('Vamos jogar novamente...')
        print('-' * 40)
    elif s % 2 != 0 and pi in 'Ii' or s % 2 != 0 and pi in 'Ii':
        print('IMPAR')
        print('-' * 40)
        print('VOCÊ VENCEU')
        print('Vamos jogar novamente...')
        print('-' * 40)
    else:
        c += -1
        if s % 2 == 0:
            print('PAR')
        else:
            print('IMPAR')
        print('Você PERDEU! :(')
        print('-=' * 20)
        print(f'GAME OVER!! Você venceu {c} vezes.')
        break
