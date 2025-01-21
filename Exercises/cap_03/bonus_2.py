# Em um sistema de avaliação de restaurante cinco estrelas (⭐️⭐️⭐️⭐️⭐️), as estrelas geralmente representam os diferentes níveis de satisfação.

# Mas o que cada uma das estrelas significa?

# Comece criando uma variável de avaliação e defina-a igual a um número decimal.

# Faça um sistema de avaliação usando uma declaração if/elif/else:

# avaliação maior que 4.5, imprima 'Extraordinário'
# avaliação maior que 4, imprima 'Excelente'
# avaliação maior que 3, imprima 'Bom'
# avaliação maior que 2, imprima 'Regular'
# Qualquer outra coisa, imprima 'Ruim'

# Solução:
# Inicializando a variável
rating = 3.5

# Rating system
if rating > 4.5:
    print('Extraordinary')
elif rating > 4:
    print('Excellent')
elif rating > 3:
    print('Good')
elif rating > 2:
    print('Fair')
else:
    print('Poor')
