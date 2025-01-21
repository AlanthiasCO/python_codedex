# Crie um programa e digite o seguinte:

# adivinhar = 0
#guess = 0

#while guess != 6:
 #   guess = int(input("Adivinhe o número:  "))

#print("Você acertou!")

# Vamos fazer com que seja o mesmo jogo de adivinhação, mas com um novo limite para o número de tentativas
# (antes era infinito).
# Primeiro, introduza uma variável chamada tentativas no topo e dê a ela um valor de 0.
# Em seguida, adicione a variável tentativas ao loop while usando um operador relacional (como você fez com adivinhar).

# solução

tries = 0
guess = 0

while guess != 6 and tries < 3:
    guess = int(input("Adivinhe o número:  "))
    tries += 1

if guess == 6:
    print("Você acertou!")
else:
    print("Você perdeu!")
    
# O código acima solicita ao usuário que adivinhe um número. 
# Se o número inserido for 6, o programa imprimirá "Você acertou!".
# Caso contrário, o programa imprimirá "Você perdeu!".
# O programa permite que o usuário faça no máximo 3 tentativas.