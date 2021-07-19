# Tabuada 3.0
t = 0
while True:
    t = int(input('Você quer ver a tabuada de qual valor? '))
    if t < 0:
        print('Finalizando o programa...')
        break
    for c in range(1, 11):
        m = t * c
        print(f'{t} x {c} = {m}')
    print('-' * 40)


