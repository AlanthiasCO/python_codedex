# Erros em Python
# Veja o exemplo abaixo:

#butterfl"ies = 10
#beetles = 12
#ladybugs = 20

#print('I caught ' + butterflies + ' 🦋 butterflies!')
#print('I caught ' + beetles + ' 🪲 beetles!')
#print('I caught ' + ladybug + ' 🐞 ladybugs!)

#print('I caught ' + str(total) + ' total bugs!'


# O código acima contém vários erros. Você consegue identificá-los?

# Erro 1: Concatenação de string e int
# O primeiro erro é que você não pode concatenar uma string e um número. Você precisa converter o número em uma string antes de concatená-lo. 
# Para corrigir isso, você pode usar a função str() para converter o número em uma string.

# Erro 2: Variável indefinida
# O segundo erro é que você está tentando imprimir uma variável que não foi definida.

# Erro 3: Parênteses ausentes
# O terceiro erro é que você esqueceu de fechar as aspas na última linha.

# Correção: 
butterflies = 10
beetles = 12
ladybugs = 20

print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

total = butterflies + beetles + ladybugs

print('I caught ' + str(total) + ' total bugs!')
# Output:
# I caught 10 🦋 butterflies!
# I caught 12 🪲 beetles!
# I caught 20 🐞 ladybugs!
# I caught 42 total bugs!
# Agora o código está corrigido e deve funcionar corretamente.