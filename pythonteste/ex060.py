# Calculo do Fatorial
import math
num = int(input('Informe um numero para calcular seu fatorial: '))
fatorial = math.factorial(num)
print(f'Calculando o fatorial de {num}!: ')
c = num
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    c -= 1
print(fatorial)