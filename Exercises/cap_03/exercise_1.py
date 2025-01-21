# No capítulo "Fluxo de Controle", exploraremos como os programas "tomam decisões" avaliando diferentes condições. E comece a introduzir lógica em nosso código!
# Antes de mergulharmos profundamente em algo chamado an if statement, vamos fazer uma demonstração divertida usando uma simulação de lançamento de moeda!

# Exercício 1: Criar um programa e digite o seguinte

#import random

#num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

#if num > 0.5:
#  print('Heads')
#else:
#  print('Tails')

#Nota: Vamos aprender mais sobre random e .randint() mais adiante no capítulo.

#Tudo o que você precisa saber é que este programa simula um lançamento de moeda:

#≈ 50% das vezes, são "Cabeças".
#≈ 50% das vezes, é "Caudas".


#Execute o programa 5 vezes para ter um gostinho do if/else declaração!

#Quantas vezes foi Heads?

# Solução:
import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
    print('Heads')
else:
    print('Tails')

# Output: Heads ou Tails
