# Extraindo Dados de Uma Lista
num = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    resp = str(input('Deseja continuar? S/N '))
    if resp in 'Nn':
        break
num.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(num)} elementos')
print(f'Lista com valores em ordem decrescente: {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não pertence a lista')