# Suponha que as férias estejam chegando e que os elfos do Pólo Norte precisem de sua ajuda para ter milhares de brinquedos LEGO embalados e prontos para envio.

# Criar um inventário.py programa com a seguinte lista:

# lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

# Cada item da lista é a quantidade de uma peça colorida para um brinquedo LEGO.

# Você pode descobrir as seguintes informações usando funções de lista integradas?

# Em qual parte do LEGO os elfos estão com pouca carga? Usar min() para descobrir.
# Existe uma parte LEGO que os elfos estão a sobrepovoar? Usar max() para descobrir

# codigo:

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print('peça com menor quantidade:', min(lego_parts))
print('peça com maior quantidade:', max(lego_parts))
print('quantidade total de peças:', sum(lego_parts))
print('quantidade de peças:', len(lego_parts))

