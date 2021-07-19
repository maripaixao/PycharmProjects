num = int(input('Escolha um número para conversão: '))
print('\033[34m1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal\033[m')
escolha = int(input('Escolha uma das opções acima: '))
if escolha == 1:
    print(f"Numero {num} convertido em Binário: \033[35m{bin(num)[2:]}\033[m")
elif escolha == 2:
    print(f'Numero {num} convertido em Octal: \033[35m{oct(num)[2:]}\033[m')
elif escolha == 3:
    print(f'Numero {num} convertido em Hexadecimal: \033[35m{hex(num)[2:]}\033[m')
else:
    print('\033[31mCondição INVALIDA\033[m')
