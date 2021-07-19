# Detector de Maioridade
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {pessoa}ª pessoa: '))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Tivemos {maior} pessoas maiores de idade')
print(f'E {menor} pessoas menores de idade')
