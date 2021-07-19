# Lista com pares e impares

valor = 0
num = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[1].sort()
num[0].sort()
print(f'Lista dos números pares: {num[0]}')
print(f'Lista dos números impares: {num[1]}')