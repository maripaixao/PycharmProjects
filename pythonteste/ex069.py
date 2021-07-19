# Análise de Dados do Grupo
maiores_dezoito = homens = mulheres_vinte = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F] ')).upper()
    print('-' * 30)
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N] ')).upper()
    if idade >= 18 and sexo in 'MmFf':
        maiores_dezoito += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres_vinte += 1
    if sn in 'Nn':
        break
print('-' * 30)
print(f'Foram cadastradas {maiores_dezoito} pessoas maiores de 18 anos,\n{homens} homens e {mulheres_vinte} mulheres abaixo dos 20 anos.')
