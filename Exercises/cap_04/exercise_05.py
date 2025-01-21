# "99 Bottles of Beer" é uma velha canção que crianças irritantes, ops, quero dizer, todos, cantavam em viagens de carro para passar o tempo.
# 
# Crie um programa chamado 99_bottles.py e use um loop for e a função range() para imprimir todos os versos de "99 Bottles of Beer."
# -------------------------------
# 99 garrafas de cerveja na parede
# 99 garrafas de cerveja
# Tire uma, passe adiante
# 98 garrafas de cerveja na parede
# ----------------------
# E não se esqueça de usar interpolação de strings!

# Solução:
for i in range(99, 0, -1):
    print(f"{i} garrafas de cerveja na parede")
    print(f"{i} garrafas de cerveja")
    print("Tire uma, passe adiante")
    print(f"{i - 1} garrafas de cerveja na parede")
    print()
# O código acima imprime todos os versos de "99 Bottles of Beer" usando interpolação de strings.
# O loop for começa em 99 e termina em 1, decrementando de 1 em 1.
# Cada verso é impresso em uma nova linha.
# O código imprime 99 versos no total.
