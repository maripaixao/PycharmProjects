# Numeros primos
n = int(input('Digite um numero: '))
mult = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
if mult == 2:
    print('\n\033[mÉ um numero primo')
else:
    print('\n\033[mNão é um numero primo')
