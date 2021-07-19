from time import sleep
print('=' * 60)
print("\033[33mREALIZE SEU SONHO DA CASA PROPRIA, FAÇA HOJE UM IMPRESTIMO!!\033[m")
print('=' * 60)
casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
sal = float(input('Quanto você recebe por mes? R$'))
anos = int(input('Em quanto tempo pretende quitar a divida? '))
prest = casa / (anos * 12)
print()
print('\033[34mProcessando...\033[m')
sleep(3)
print()
print(f'Para a compra de uma casa no valor de R${casa} financiada em {anos} anos, a prestação ficaria no valor de R${prest:.2f}')
if prest <= (sal * 30) / 100:
    print(f'\033[32mPARABÉNS, será possivel financiar a casa\ncom parcelas mensais no valor de R${prest:.2f}durante {anos} anos\033[m')
else:
    print("\033[31mInfelizmente seu emprestimo foi NEGADO\033[m")