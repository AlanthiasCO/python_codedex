""" 
Crie um programa chamado dry.py e confira a lista completa de funções embutidas:

Encontre 4 funções embutidas que usamos anteriormente no curso.
Escolha 1 função embutida que não vimos antes.
Use cada uma dessas funções uma vez no programa.

Para a nova função, tente ler a documentação (😵‍💫) ou pesquise no Google (👍)!

Adicione um comentário para cada função embutida explicando como elas funcionam.
"""

# Solucao:  

# 1. Usando a funcção reserver() para inverter a ordem de uma lista
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


# 2. Usando a função sort() para ordenar uma lista
my_list_sort = [5, 3, 1, 2, 4]
my_list_sort.sort()
print(my_list_sort)

# 3. usando a função slice() para fatiar uma lista
my_list_slice = [1, 2, 3, 4, 5]
my_list_slice = my_list_slice[1:4]
print(my_list_slice)

# 4. Usando a função len() para contar o número de elementos em uma lista
my_list_len = [1, 2, 3, 4, 5]
print(len(my_list_len))

# 5. Usando a função sum() para somar todos os elementos de uma lista
my_list_sum = [1, 2, 3, 4, 5]
print(sum(my_list_sum))

# 6. Usando a função max() para encontrar o maior elemento de uma lista
my_list_max = [1, 2, 3, 4, 5]
print(max(my_list_max))

# 7. Usando a função min() para encontrar o menor elemento de uma lista
my_list_min = [1, 2, 3, 4, 5]
print(min(my_list_min))

# 8. Usando a função round() para arredondar um número
my_number = 3.14159
print(round(my_number, 2))

# 9. Usando a função abs() para encontrar o valor absoluto de um número
my_negative_number = -5
print(abs(my_negative_number))

# 10. Usando a função pow() para elevar um número a uma potência
my_number = 2
print(pow(my_number, 3))

# 11. Usando a função all() para verificar se todos os elementos de uma lista são verdadeiros
my_list_all = [True, True, False]
print(all(my_list_all))

# 12. Usando a função any() para verificar se algum elemento de uma lista é verdadeiro
my_list_any = [False, False, True]
print(any(my_list_any))

# 13. Usando a função enumerate() para obter o índice e o valor de cada elemento de uma lista
my_list_enumerate = ['a', 'b', 'c']
for index, value in enumerate(my_list_enumerate):
    print(f'Index: {index}, Value: {value}')

# 14. Usando a função filter() para filtrar os elementos de uma lista com base em uma função
def is_even(number):
    return number % 2 == 0

my_list_filter = [1, 2, 3, 4, 5]
filtered_list = list(filter(is_even, my_list_filter))
print(filtered_list)

# 15. Usando a função map() para aplicar uma função a cada elemento de uma lista
def square(number):
    return number ** 2

my_list_map = [1, 2, 3, 4, 5]
squared_list = list(map(square, my_list_map))
print(squared_list)
