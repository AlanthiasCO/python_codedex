# Desde 1927, a montanha-russa "The Cyclone" tem encantado os visitantes em Coney Island (Brooklyn, NY). 🎢
#
# Eles estão agora instalando um novo sistema de entrada (o requisito de altura é 1.37 cm e o custo é 10 créditos) e precisam da sua ajuda para escrever o programa para isso!
#
# Crie um novo arquivo chamado the_cyclone.py.
#
# Pergunte ao usuário qual é a sua altura e quantos créditos ele tem, e armazene os valores em uma variável de altura e uma variável de créditos.
#
# Use uma combinação de operadores relacionais e lógicos para criar as regras:
#
# Se eles forem altos o suficiente e tiverem créditos suficientes, imprima "Aproveite o passeio!"
# Caso eles tenham créditos suficientes, mas não sejam altos o suficiente, imprima "Você não tem altura suficiente para andar."
# Caso eles sejam altos o suficiente, mas não tenham créditos suficientes, imprima "Você não tem créditos suficientes."
# Caso contrário, imprima uma mensagem dizendo que eles não atenderam a nenhum dos requisitos.

# Solução:
altura = float(input('Qual é a sua altura em cm? '))
creditos = int(input('Quantos créditos você tem? '))
if altura >= 1.37 and creditos >= 10:
    print('Aproveite o passeio!')
elif altura < 1.37 and creditos >= 10:
    print('Você não tem altura suficiente para andar.')
elif altura >= 1.37 and creditos < 10:
    print('Você não tem créditos suficientes.')
else:
    print('Você não atende a nenhum dos requisitos.')

