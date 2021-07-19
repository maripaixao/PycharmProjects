# Dividindo Valores em Várias Listas
valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? S/N '))
    if resp in 'Nn':
        break
for i, n in enumerate(valores):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
print('-=' * 25)
print(f'Lista completa: {valores}')
print(f'Lista com valores pares: {par}')
print(f'Lista com valores impares: {impar}')