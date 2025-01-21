# Escreva um programa que use declarações if aninhadas para determinar se é um bom dia para ir à praia.
# O programa deve verificar se o tempo está ensolarado e a umidade é menor que 60.
# Se ambas as condições forem atendidas, o programa deve imprimir 'Vamos à praia! 🏖️'.
# Se o tempo estiver ensolarado, mas a umidade for 60 ou maior, o programa deve imprimir 'Hmmm, está um pouco úmido para um dia de praia.'.

weather = 'Sunny'
humidity = 35

if weather == 'Sunny':
  if humidity < 60:
    print('Let’s go to the beach! 🏖️')
  else:
    print('Hmmm, it’s a little humid for a beach day.')
else:
  print('It’s not sunny today... let’s try for another day.')