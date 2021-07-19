pessoas = dict()
cadastro = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Digite seu nome: "))
    pessoas['idade'] = int(input("Informe sua idade: "))
    while True:
        pessoas['sexo'] = str(input("Sexo F/M: ")).upper()[0]
        if pessoas['sexo'] in 'FfMm':
            break
        print("Inválido! Por favor, digite apenas F ou M.")
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    while True:
        opc = str(input('Deseja continuar? S/N ')).upper()[0]
        if opc in 'SN':
            break
        print('Inválido! Por favor, responda apenas S ou N.')
    if opc == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = soma / len(cadastro)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ,', end='')
print()
print('Lista das pessoas acimas da média: ')
for p in cadastro:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
            print()
print('>>> ENCERRADO <<<')
