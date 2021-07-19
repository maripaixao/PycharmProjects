from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
ranking = list()
jogadas['j1'] = int(randint(1, 6))
jogadas['j2'] = int(randint(1, 6))
jogadas['j3'] = int(randint(1, 6))
jogadas['j4'] = int(randint(1, 6))
print('Números sorteados: ')
for k, v in jogadas.items():
    print(f'O {k} tirou: {v}')
    sleep(1)
print('-=' * 20)
print("RANKING")
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
