# Detector de Palindromo
frase1 = str(input('Digite uma frase qualquer: ')).replace(' ', '')
frase2 = frase1[::-1]
if frase1 == frase2:
    print('É um PALINDROMO')
else:
    print('NAO é um PALINDROMO')
