dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))

if dados['media'] < 7:
    dados['status'] = 'Reprovado'
else:
    dados['status'] = 'Aprovado'

print('-=' * 30)
for k, v in dados.items():
    print(f'O {k} é igual a {v}')
