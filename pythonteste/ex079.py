# Valores Unicos em uma Lista
num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Deseja continuar? S/N ')).upper().strip()
    if resp in 'Nn':
        break
num.sort()
print(f'Você digitou os valores: {num}')