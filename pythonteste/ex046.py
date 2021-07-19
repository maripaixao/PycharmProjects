# Contagem Regressiva
from time import sleep
from pyemojify import emojify
for c in range(10, -1, -1):
    print(c,'...')
    sleep(1)
print(emojify(' :fireworks: :fireworks: \033[33mFELIZ ANO NOVO!!!!\033[m :fireworks: :fireworks: '))
