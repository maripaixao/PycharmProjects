from datetime import datetime

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)

print('-=' * 30)
for k, v in cadastro.items():
    print(f'    - {k} tem valor {v}')
