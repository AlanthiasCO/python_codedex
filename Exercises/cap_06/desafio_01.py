# In some online multiplayer games, there's a KDA ratio to evaluate a player's in-game performance:
#
# KDA=(k+a)/d
#
# k is how many players you took down.
# d is how many times you died.
# a is how many assists you had.
# Write a kda() function that takes in parameters: k, d, a.
#
# This function should calculate and return the KDA ratio that uses these parameters.

# solucao:

def kda(k, d, a):
    return (k + a) / d

print(kda(5, 2, 3))  # 4.0
print(kda(10, 5, 5))  # 3.0
print(kda(2, 1, 1))  # 3.0
print(kda(1, 1, 1))  # 2.0

