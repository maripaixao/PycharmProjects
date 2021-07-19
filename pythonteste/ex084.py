# Lista Composta e Análise de Dados

temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Informe seu peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')