# Expoente de um número. Python também pode realizar exponenciação como 2³ ou 10².

# Exemplo:
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32

# -----------------------------------------------------------------------------------------------------------------------

# Exercício 3:
#Criar um programa que calcula seu próprio IMC.
# IMC é a sigla para Índice de Massa Corporal. É uma medida que usa a altura e o peso para determinar se uma pessoa tem um peso saudável.

# A fórmula para calcular o IMC é: peso(kg) / altura(m)²

# Solução:
peso = 80
altura = 1.87
imc = peso / (altura ** 2)
print('IMC:', imc) 