# Criando Menu de Opções
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = 0
maior = 0
while menu != 5:
    print('Selecione uma opção: \n[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Mostrar o maior valor \n[ 4 ] Selecionar novos valores \n[ 5 ] Sair do programa\n')
    menu = int(input('Selecione sua opção: '))
    if menu == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif menu == 2:
        mult = num1 * num2
        print(f'{num1} x {num2} = {mult}')
    elif menu == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print(f'Entre {num1} e {num2}, o maior valor é {maior}')
    elif menu == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida! Tente novamente')
    print('-=' * 10)
print('Volte sempre!')