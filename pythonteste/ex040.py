from time import sleep
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Calculando...')
sleep(2)
print(f'Sua média foi {media}')
if media < 5.0:
    print(f"\033[31mVocê foi reprovado. Estude mais!\033[m")
elif media == 5.0 or media < 6.9:
    print(f'\033[33mVoce está de recuperação\033[m')
else:
    print(f'\033[34mParabéns, você foi aprovado!!')