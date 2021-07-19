r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 < r3 or r2 + r3 < r1 or r1 + r3 < r2:
    print('Estes segmentos NAO formam um triangulo')
elif r1 == r2 == r3:
    print('É possivel formar um triangulo EQUILATERO')
elif r1 != r2 != r3 != r1:
    print('É possivel formar um triangulo ESCALENO')
else:
    print('É possivel formar um triangulo ISOSCELES')