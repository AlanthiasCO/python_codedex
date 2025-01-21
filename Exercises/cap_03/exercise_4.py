# Exercicio 4:
# O Bola 8 mágica é um brinquedo de escritório popular e um brinquedo infantil inventado na década de 1940 para adivinhação e busca de conselhos. 🎱
#
# É uma bola 8 de grandes dimensões com algumas das seguintes respostas:
#
# Sim - definitivamente.
# É decididamente assim.
# Sem dúvida.
# Resposta vaga, tente novamente.
# Pergunte novamente mais tarde.
# Melhor não te contar agora.
# Minhas fontes dizem que não.
# Perspectiva não é boa.
# Muito duvidoso.
# Criar um magia8.py programa que pode responder a quaisquer perguntas Sim ou Não com uma resposta diferente cada vez que é executado.
#
# A saída deverá ter o seguinte formato:
#
# Pergunta:      [Pergunta]
# Bola 8 Mágica: [Resposta]

# solução:

import random

pergunta = input('Pergunta: ')
resposta = random.randint(1, 8)

if resposta == 1:
    coringa = 'Sim - definitivamente.'
elif resposta == 2:
    coringa ='É decididamente assim.'
elif resposta == 3:
    coringa ='Sem dúvida.'
elif resposta == 4:
    coringa ='Resposta vaga, tente novamente.'
elif resposta == 5:
    coringa ='Pergunte novamente mais tarde.'
elif resposta == 6:
    coringa ='Melhor não te contar agora.'
elif resposta == 7:
    coringa ='Minhas fontes dizem que não.'
elif resposta == 8:
    coringa ='Perspectiva não é boa.'
else:
    coringa = "Erro"

print('Bola 8 Mágica:', coringa)
