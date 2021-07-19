# Maior e menor valores
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros e a media entre eles é {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
