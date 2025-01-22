"""
Já se perguntou quantas pessoas vivem na cidade de Nova York? E em Londres?

Crie um programa chamado favorite_cities.py.

Vamos criar uma classe Cidade que usa o método __init__() para definir os seguintes atributos:

nome (string)
país (string)
população (inteiro arredondado para o milhar mais próximo)
pontos turísticos (lista de strings)
Em seguida, crie um objeto para sua cidade natal e atribua os atributos acima.

Por fim, crie outro objeto da cidade que você sempre quis visitar!

Bônus: Adicione 2-3 atributos adicionais, como apelido, ano de fundação, prefeito, etc.
"""

# solucao:
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks


nyc = City("New York City", "USA", 8468000, ["Statue of Liberty", "Brooklyn Bridge", "Apollo Theatre"])
london = City('London', 'UK', 8900000, ['Big Ben', 'Buckingham Palace', 'Tower Bridge'])
shanghai = City("Shanghai", "China", 26320000, ["The Bund", "Jin Mao Tower", "Tianzifang"])

print(vars(nyc))
print(vars(shanghai))
print(vars(london))

