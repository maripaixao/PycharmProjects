nome = str(input('Qual é seu nome? '))
if nome == 'Marina':
    print('Que nome bonito!')
elif nome == 'Fernanda':
    print('Seu nome é bem comum.')
elif nome in 'Maria' or 'Isabela' or 'Silva':
    print('Seu nome é popular no Brasil')
print(f'Tenha um bom dia, {nome}!')