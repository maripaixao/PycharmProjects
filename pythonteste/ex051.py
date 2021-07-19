# Progressao Aritmetica
n = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
u = n + (10-1)*r
for c in range(n, u+1, r):
    print(c, end=' >> ')
