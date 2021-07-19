altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / altura ** 2
print(f'Seu IMC é de: {imc:.1f}')
if imc < 18.5:
    print('\033[33mVoce esta ABAIXO DO PESO\033[m')
elif imc == 18.5 or imc <= 25:
    print('\033[32mVoce esta no PESO IDEAL\033[m')
elif imc == 25 or imc <= 30:
    print('\033[33mVoce esta em SOBREPESO\033[m')
elif imc == 30 or imc <= 40:
    print('\033[31mVoce esta com OBESIDADE\033[m')
else:
    print('\033[31mOBESIDADE MORBIDA\033[m')