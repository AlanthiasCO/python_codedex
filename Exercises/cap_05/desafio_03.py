#Todos os anos no Oscar, o Oscar de Melhor Filme é concedido a um único filme. Geralmente é o último prêmio entregue e é considerado o de maior prestígio.
#Vamos usar uma lista Python para documentar os vencedores recentes!

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist',
  '2010 - The King\'s Speech'
]

# adicione os melhores filmes de 2020 até 2022 na frente da lista, veja os filmes:
# melhor filme de 2020: Nomadland
# melhor filme de 2021: CODA
# melhor filme de 2022: Everything Everywhere All at Once

best_pictures.insert(0, '2020 - Nomadland')
best_pictures.insert(0, '2021 - CODA')
best_pictures.insert(0, '2022 - Everything Everywhere All at Once')

# imprima a lista atualizada
print(best_pictures)
