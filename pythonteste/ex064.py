# Tratando vários valores
cont = 0
soma = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')
