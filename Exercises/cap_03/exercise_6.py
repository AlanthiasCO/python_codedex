# O Chapéu Seletor é um chapéu mágico falante na Escola de Magia e Bruxaria de Hogwarts. 
# O chapéu decide para qual das quatro "Casas" cada aluno do primeiro ano vai:

# 🦁 Grifinória
# 🦅 Corvinal
# 🦡 Lufa-Lufa
# 🐍 Sonserina

# Escreva um programa que faça algumas perguntas ao usuário com as funções int() e input():

# Q1) Você prefere Amanhecer ou Anoitecer?
#     1) Amanhecer
#     2) Anoitecer

# Se a resposta for igual a 1, Grifinória e Corvinal recebem +1.
# Caso contrário, se a resposta for igual a 2, Lufa-Lufa e Sonserina recebem +1.
# Caso contrário, exiba a mensagem "Entrada errada."

# Q2) Quando eu morrer, quero que as pessoas me lembrem como:
#     1) O Bom
#     2) O Grande
#     3) O Sábio
#     4) O Corajoso

# Se a resposta for 1, Lufa-Lufa +2.
# Caso contrário, se a resposta for 2, Sonserina +2.
# Caso contrário, se a resposta for 3, Corvinal +2.
# Caso contrário, se a resposta for 4, Grifinória +2.
# Caso contrário, exiba a mensagem "Entrada errada."

# Q3) Qual tipo de instrumento mais agrada seu ouvido?
#     1) O violino
#     2) A trombeta
#     3) O piano
#     4) O tambor

# Se a resposta for 1, Sonserina +4.
# Caso contrário, se a resposta for 2, Lufa-Lufa +4.
# Caso contrário, se a resposta for 3, Corvinal +4.
# Caso contrário, se a resposta for 4, Grifinória +4.
# Caso contrário, exiba "Entrada errada."

# Por fim, imprima a pontuação de cada casa.

# Bônus: Se você quiser ir além, veja se consegue descobrir como imprimir a casa com mais pontos!

# Solução:

# Inicializando as variáveis
grifinoria = 0
corvinal = 0
lufa_lufa = 0
sonserina = 0

# Perguntas
q1 = int(input("Você prefere Amanhecer ou Anoitecer?\n1) Amanhecer\n2) Anoitecer\n"))
if q1 == 1:
    grifinoria += 1
    corvinal += 1
elif q1 == 2:
    lufa_lufa += 1
    sonserina += 1
else:
    print("Entrada errada.")

q2 = int(input("Quando eu morrer, quero que as pessoas me lembrem como:\n1) O Bom\n2) O Grande\n3) O Sábio\n4) O Corajoso\n"))
if q2 == 1:
    lufa_lufa += 2
elif q2 == 2:
    sonserina += 2
elif q2 == 3:
    corvinal += 2
elif q2 == 4:
    grifinoria += 2
else:
    print("Entrada errada.")

q3 = int(input("Qual tipo de instrumento mais agrada seu ouvido?\n1) O violino\n2) A trombeta\n3) O piano\n4) O tambor\n"))
if q3 == 1:
    sonserina += 4
elif q3 == 2:
    lufa_lufa += 4
elif q3 == 3:
    corvinal += 4
elif q3 == 4:
    grifinoria += 4
else:
    print("Entrada errada.")

# Imprimindo a pontuação de cada casa
print("\nPontuação das casas:")
print(f"Grifinória: {grifinoria}\nCorvinal: {corvinal}\nLufa-Lufa: {lufa_lufa}\nSonserina: {sonserina}")

# Imprimindo
if grifinoria > corvinal and grifinoria > lufa_lufa and grifinoria > sonserina:
    print("\nGrifinória venceu!")
elif corvinal > grifinoria and corvinal > lufa_lufa and corvinal > sonserina:
    print("\nCorvinal venceu!")
elif lufa_lufa > grifinoria and lufa_lufa > corvinal and lufa_lufa > sonserina:
    print("\nLufa-Lufa venceu!")
elif sonserina > grifinoria and sonserina > corvinal and sonserina > lufa_lufa:
    print("\nSonserina venceu!")
else:
    print("\nEmpate!")
