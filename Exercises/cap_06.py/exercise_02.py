# Biscoito da Sorte é um pequeno wafer de biscoito com um pedaço de papel dentro, chamado de "fortuna", que geralmente é uma frase chinesa com tradução e uma lista de números da sorte. Eles são servidos em restaurantes nos EUA e no Canadá.
# Crie um programa que dê ao usuário fortunas aleatórias.
# Defina uma função chamada fortune().
# Dentro da função, imprima uma fortuna aleatória da lista de opções abaixo:

# Não persiga a felicidade – crie-a.
# Todas as coisas são difíceis antes de serem fáceis.
# O pássaro madrugador pega a minhoca, mas o segundo rato pega o queijo.
# Alguém na sua vida precisa de uma carta sua.
# Não apenas pense. Aja!
# Seu coração vai pular uma batida.
# A fortuna que você procura está em outro biscoito.
# Socorro! Estou sendo mantido prisioneiro em uma padaria chinesa!
# Certifique-se de usar o random.randint() do módulo random e um if/elif/else.

# Em seguida, chame a função fortune() três vezes e veja o que você obtém!

# Bônus: Se você for ousado, reescreva a função sem um if/elif/else.

# Solucao:
import random

def fortune():
    fortunes = [
        'Não persiga a felicidade, crie-a.',
        'Todas as coisas são difíceis antes de serem fáceis.',
        'O pássaro madrugador pega a minhoca, mas o segundo rato pega o queijo.',
        'Alguém na sua vida precisa de uma carta sua.',
        'Não apenas pense. Aja!',
        'Seu coração vai pular uma batida.',
        'A fortuna que você procura está em outro biscoito.',
        'Socorro! Estou sendo mantido prisioneiro em uma padaria chinesa!'
    ]
    print(random.choice(fortunes))

fortune()