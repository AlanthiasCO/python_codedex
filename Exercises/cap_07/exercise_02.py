"""
No último exercício, criamos uma classe Restaurante.

Em um novo arquivo chamado bobs_burgers.py, crie uma instância da classe Restaurante chamada bobs_burgers com os seguintes atributos:

'Bob\'s Burgers'
'Diner Americano'
4.7
False
Depois disso, crie mais duas instâncias da classe Restaurante com seus restaurantes favoritos próximos.

Em seguida, use print(vars()) para exibir cada um dos três restaurantes!

"""


# solucao:

from exercise_01 import Restaurant

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'Diner Americano'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False


katz_deli = Restaurant()
katz_deli.name = 'Katz\'s Deli'
katz_deli.type = 'Kosher Deli'
katz_deli.rating = 4.5
katz_deli.delivery = True

baekjeong = Restaurant()
baekjeong.name = 'Baekjeong NYC'
baekjeong.type = 'Korean BBQ'
baekjeong.rating = 4.4
baekjeong.delivery = False

print(vars(bobs_burgers))
print(vars(katz_deli))
print(vars(baekjeong))


print(vars(bobs_burgers))
print(vars(katz_deli))
print(vars(baekjeong))
