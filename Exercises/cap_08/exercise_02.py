"""
Vamos colocar nosso conhecimento recém-adquirido sobre as palavras-chave from e as à prova, descobrindo as áreas de superfície dos planetas em nosso sistema solar! 🪐

Crie um novo arquivo chamado solar_system.py.

Em seguida, importe o seguinte no topo do arquivo:

Do módulo math, a variável pi (π).
Do módulo random, o método .choice(), renomeado como ch para abreviar.
Depois, copie e cole a seguinte lista:

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

Em seguida, use o método ch() para obter uma string aleatória de planets e atribua-a a uma variável chamada random_planet.

E use a variável pi (π) importada para calcular a área de superfície de uma esfera:

area=4πr²

Para fazer isso, precisaremos saber o raio r para um dado random_planet (arredondado para o quilômetro mais próximo).

Escreva uma declaração if/elif/else e atribua um valor a r com o seguinte em mente:

Se random_planet for 'Mercury', então r é 2440.
Senão, se random_planet for 'Venus', então r é 6052.
Senão, se random_planet for 'Earth', então r é 6371.
Senão, se random_planet for 'Mars', então r é 3390.
Senão, se random_planet for 'Saturn', então r é 58232.
Senão, imprima "Oops! An error occurred." no console.
Por fim, calcule a área e imprima o nome do random_planet junto com sua área no console.

Bônus: Os resultados calculados podem parecer um pouco longos. Existe uma função embutida em Python que pode arredondá-los?

"""

# solucao:

import math
from random import choice as ch

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232

area = 4 * math.pi * r ** 2

print(f"A área de superfície de {random_planet} é {round(area, 2)} km².")
