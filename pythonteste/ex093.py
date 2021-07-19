jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for i in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {i+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas e fez {jogador["total"]} gols.')