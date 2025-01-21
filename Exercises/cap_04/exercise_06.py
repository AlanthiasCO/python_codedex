# Fizz Buzz é um jogo de palavras infantil que ensina divisão. Também é uma questão clássica de entrevista técnica em inúmeras empresas. 🐝
# Embora este desafio possa parecer simples para programadores experientes, ele é projetado para eliminar 90% dos candidatos a emprego que não conseguem aplicar seu conhecimento de codificação a um novo problema de forma criativa. Quer tentar?

# Crie um programa fizz_buzz.py que exiba números de 1 a 100.

# Aqui está o desafio:

# Para múltiplos de 3, imprima "Fizz" em vez do número.
# Para múltiplos de 5, imprima "Buzz" em vez do número.
# Aqui está a parte complicada: Para múltiplos de 3 e 5, imprima "FizzBuzz".
# A saída deve ser assim:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...

# A propósito, está tudo bem se você não conseguir resolver este... é um problema difícil! Dê uma olhada na dica e na solução antes de seguir para o Projeto de Checkpoint! ⛳️

# Solução:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# O código acima imprime números de 1 a 100.
# Para múltiplos de 3, o código imprime "Fizz".
# Para múltiplos de 5, o código imprime "Buzz".
# Para múltiplos de 3 e 5, o código imprime "FizzBuzz".
# O código imprime a saída correta para os números de 1 a 100.