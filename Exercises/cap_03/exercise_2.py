# Condição IF é uma estrutura de controle que permite avaliar uma expressão e, dependendo do resultado, executar um bloco de código.
# a expressão é avaliada como True ou False. 
# Se a expressão for True, o bloco de código dentro do if statement é executado.
# Se a expressão for False, o bloco de código dentro do else statement é executado.

# Exemplo:

# if condition:
  # code inside

# -------------------------------------------------------

# Exemplo: se o valor for maior que 60
#if grade > 60:
  #print("You passed!")

# continuação
#if grade > 60:
 # print("You passed.")
#else:
 # print("You failed.")

# -------------------------------------------------------

# Exercício 2: Criar um programa que verifica se uma nota está acima ou abaixo de 55. Comece criando uma variável chamada grade e dê-lhe um valor entre 0-100.
#Escreva a if/else declaração para o seguinte:
#Se a nota for maior ou igual a 55, então imprima "Você passou"
#Caso contrário, imprima "Você falhou"


# Solução:

grade = 60

if grade >= 55:
    print('Você passou')
else:
    print('Você falhou')

    