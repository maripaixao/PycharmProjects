from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = str(input('F - Feminino\nM - Masculino\nSexo: ')).upper()
atual = date.today().year
idade = atual - ano
if sexo == 'F':
        print('Alistamento militar OPCIONAL')
elif idade < 18:
    print('\033[33mVocê ainda vai se alistar ao serviço militar. Aguarde')
    print(f'Faltam {18 - idade} anos\033[m')
elif idade == 18 and sexo == 'M':
    print('Alistamento militar OBRIGATORIO')
    print('\033[32mJá está na hora de se alistar\033[m')
else:
    print('\033[31mJa passou do prazo de alistamento')
    print(f'Atraso de {idade - 18} anos\033[m')
