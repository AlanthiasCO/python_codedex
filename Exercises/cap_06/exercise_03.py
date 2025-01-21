# Em setembro de 1999, após dez meses de viagem para Marte, o Mars Climate Orbiter de repente se desintegrou porque entrou na atmosfera muito rápido.

# Oh não! Os engenheiros da NASA esqueceram de converter os dados imperiais para dados métricos em uma das funções! Esse erro de principiante custou aos contribuintes americanos um total de $125 milhões.

# Suponha que você é um estagiário da NASA, e sua equipe está calculando a distância que um foguete precisa viajar. O valor calculado está em quilômetros, enquanto o próximo passo requer milhas. Seu gerente rapidamente escreve isso no quadro:

# miles = kilometer / 1.609

# Crie um novo arquivo chamado rocket.py.

# Defina uma função chamada distance_to_miles() que converte uma distância de quilômetros para milhas. Ela deve:

# Receber um parâmetro chamado distance (a distância em quilômetros).
# Imprimir a distância em milhas.
# Depois, chame a função e use 10000 como argumento.

# solucao:

def distance_to_miles(distance):
    miles = distance / 1.609
    print(miles)

distance_to_miles(10000)

# Output: 6213.712005577142
