#Crie duas listas vazias chamadas my_numbers e winning_numbers.
#Loop sobre um intervalo de 5 passos (ou seja, range(0,5)) e preencher ambas as listas com um número 
# aleatório entre 1 e 69.
#Fora do loop, adicione mais um número a cada lista que esteja entre 1 e 26.
#Por último, imprima o my_numbers e winning_numbers listas para o terminal. A saída poderia ser assim:

# Solucao:
import random

my_numbers = []
winning_numbers = []

for _ in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))

my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

print(my_numbers)
print(winning_numbers)

