# Operadores Relacionais
# Muitas vezes dentro das condições, estamos comparando dois valores. Para tanto, precisamos utilizar um tipo diferente de operadores chamados operadores
# relacionais que compara valores:

# == igual a
# != não igual a
# > maior que
# < menos de
# >= maior ou igual a
# <= menor ou igual a

# Elif
# Um ou mais elif instruções (abreviação de "else if") podem ser opcionalmente adicionadas entre o if e else para fornecer condição(ões) adicional(is) para verificar.
# Às vezes, dois simplesmente não é suficiente.

# if grade > 90:
#  print('A')
# elif grade > 80:
#  print('B')
# elif grade > 70:
#  print('C')
# elif grade > 60:
#  print('D')
# else:
#  print('F')


# Exercício 3:
# Criar um programa que verifica se um nível de pH é básico, ácido ou neutro. Primeiro, crie um ph variável e peça ao usuário um valor entre 0 e 14.

# Escreva um if, elif, else declaração que:
# Se ph é maior que 7, saída "Básico".
# Se ph é inferior a 7, saída "Ácido".
# Caso contrário, saída "Neutro".

# Solução:

ph = float(input('Digite um valor de pH entre 0 e 14: '))
if ph > 7:
    print('Básico')
elif ph < 7:
    print('Ácido')
else:
    print('Neutro')

# Output: Ácido