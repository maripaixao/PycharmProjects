# Jogo da Adivinhação
from random import randint
from time import sleep
num = int(input('Estou pensando em um numero entre 0 e 10. Tente adivinhar... '))
aleatorio = randint(0, 10)
palpites = 1
print('PROCESSANDO...')
sleep(1)
while num != aleatorio:
    num = int(input('Você errou! Tente novamente '))
    print('PROCESSANDO...')
    sleep(1)
    palpites += 1
    if num < aleatorio:
        print('Mais... Tente novamente')
    elif num > aleatorio:
        print('Menos... Tente novamente')
if num == aleatorio:
    print(f'PARABÉNS!! Voce conseguiu acertar usando {palpites} palpites')
