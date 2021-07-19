# Tuplas Com Times de Futebol
times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('-='*20)
print(f'\033[034mLista dos Times do Brasileirão:\033[m \n{times}')
print('-='*20)
print(f'\033[32mOs 5 primeiros times são:\033[m \n{times[0:5]}')
print('-='*20)
print(f'\033[31mOs 4 últimos são:\033[m \n{times[-4:]}')
print('-='*20)
print(f'\033[33mTimes em ordem alfabética:\033[m \n{sorted(times)}')
print('-='*20)
if 'Chapecoense' not in times:
    print('O time não foi classificado.')
else:
    print(f'O time Chapecoense ocupa a {times.index("Chapecoense")+1}ª posição.')
