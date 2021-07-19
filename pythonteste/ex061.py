# Progressao Aritmetica 2.0
n = int(input('Primeiro termo: '))
r = int(input('Informe a razão: '))
termo = n
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    c += 1
print('FIM')