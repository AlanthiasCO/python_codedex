# Operadores aritméticos do Python: +, -, *, /, //, %, **
# +: Adição
# -: Subtração
# *: Multiplicação
# /: Divisão
# //: Divisão inteira
# %: Módulo
# **: Exponenciação

# Exemplo:
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print('Exemplo 1:', score)        # Output: 1
# -----------------------------------------------------------------------------------------------------------------------
# Exemplo:
pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print('Exemplo 2:',tip) # Output: 0.796
# -----------------------------------------------------------------------------------------------------------------------

# Exercício 2:
# Criar programa que converte um número de Fahrenheit (°F) para Celsius (°C).
# A fórmula para a conversão é: (Fahrenheit - 32)/1.8 = Celsius

# Solução:
fahrenheit = 100
celsius = (fahrenheit - 32) / 1.8
print(fahrenheit,'°Fahrenheit em °Celsius:', celsius) # Output: 37.77777777777778
# -----------------------------------------------------------------------------------------------------------------------
