from datetime import date
ano = int(input('Em que ano voce nasceu? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você esta na categoria \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Você esta na categotia \033[34mINFANTIL\033[m')
elif idade <= 19:
    print('Você esta na categoria \033[34mJUNIOR\033[m')
elif idade <= 20:
    print('Voce esta na categoria \033[34mSENIOR\033[m')
else:
    print('Voce esta na categoria \033[34mMASTER\033[m')