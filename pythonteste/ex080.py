# Lista Ordenada Sem Repetições
num = []
for cont in range(0, 5):
    numeros = int(input('Digite um valor: '))
    if cont == 0 or numeros > num[-1]:
        num.append(numeros)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if numeros <= num[pos]:
                num.insert(pos, numeros)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Você digitou os numeros: {num}')