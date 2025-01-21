#Até agora, só temos enviado coisas ao usuário, tornando nossos programas unilaterais e não tão divertidos. Quase todos os sites, aplicativos móveis ou videogames populares hoje em dia têm entrada e saída.
#A entrada é quando o usuário fornece dados ao programa. A saída é quando o programa fornece dados ao usuário.
#Para obter a entrada do usuário em Python, usamos a função input(). A função input() exibe uma mensagem ao usuário e aguarda a entrada do usuário. Quando o usuário pressiona Enter, a função input() retorna o que o usuário digitou.
# Input de dados: input()


# Exemplo:
username = input('Enter your name: ')

print(username)

# -------------------------------------------------------

# Exemplo:
age = int(input('What is your age? '))

print(age)

# -------------------------------------------------------

# Exercício 4:
# Criar um programa que pede ao utilizador dois números, a e b, e depois calcula a hipotenusa c de um triângulo retângulo usando o teorema de Pitágoras.
# O teorema de Pitágoras é: c² = a² + b²

# Solução:
a = float(input('Digite o tamanho de A: '))
b = float(input('Digite o tamanho de B: '))
c = (a ** 2 + b ** 2) ** 0.5
print('O valor da hipotenusa é:', c)
