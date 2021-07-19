#pessoas = lista que compoe o dicionario
#keys = chaves (nome, sexo, idade)
#values = valores (marina, f, 25)
#items = keys + values

'''brasil = []
estado1 = {'uf': 'Ceará', 'sigla': 'CE  '}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

