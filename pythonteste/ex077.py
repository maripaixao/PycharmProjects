# Contando Vogais em Tupla
palavras = ('LIVROS', 'VIDEO GAME', 'MUSICA', 'SERIES', 'FILMES', 'TECNOLOGIA',
            'PROGRAMACAO', 'INTERNET', 'JOGOS')
for c in palavras:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')