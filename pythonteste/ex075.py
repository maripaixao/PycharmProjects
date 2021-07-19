# Análise de Dados de uma Tupla
num = (int(input('Digite o 1º valor: ')),
       int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')),
       int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 está na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')