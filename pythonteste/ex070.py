# Estatisticas em Produtos
total = maisMil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$'))
    resp = ' '
    cont += 1
    total += preco
    while resp not in 'NS':
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
    print('-' * 30)
    if preco > 1000:
        maisMil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
print(f'Total gasto R${total:.2f}')
print(f'Foram {maisMil} produtos acima de R$1000.00')
print(f'{barato} foi o produto mais barato que custa R${menor:.2f}.')
