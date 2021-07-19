preco = float(input('Informe o preço do produto R$'))
print('1 - À vista dinheiro/cheque')
print('2 - À vista cartão')
print('3 - Parcelado 2x')
print('4 - Parcelado 3x ou mais')
escolha = int(input('Escolha a forma de pagamento: '))
if escolha == 1:
    pg = preco - ((preco * 10)/100)
    print(f'Pagamento a vista no dinheiro/cheque fica por R${pg}')
elif escolha == 2:
    pg = preco - ((preco * 5) / 100)
    print(f'Pagamento a vista no cartão fica por R${pg}')
elif escolha == 3:
    pg = preco / 2
    print(f'Pagamento parcelado em até 2x fica por R${pg}')
elif escolha == 4:
    parc = int(input('Informe a quantidade de parcelas: '))
    pg = (preco + ((preco * 20) / 100)) / parc
    atual = preco + (preco * 20) / 100
    print(f'3x ou mais no cartão fica por R${atual} em {parc}x de R${pg}')
