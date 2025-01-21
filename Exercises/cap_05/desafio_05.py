# Vamos usar uma lista Python para encontrar uma combinação específica de três letras, começando com o seguinte:

# dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

# Em seguida, defina duas variáveis:

# item_to_find string que é definida como uma combinação de três letras de sua escolha, sem espaços (por exemplo, 'TGA' ou 'CAT').
# item_found booleano, inicializado como False.
# Percorra cada item na lista dna_sequence. Dentro, use uma instrução if para testar se um determinado item é igual ao item_to_find. Se for, defina item_found como True.

# Fora do loop, use uma instrução if/else para verificar se item_found é True:

# Se for, imprima algo como "Item Encontrado!"
# Caso contrário, imprima algo como "Item não encontrado."

# Solucao:
dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = 'CAT'
item_found = False

for item in dna_sequence:
    if item == item_to_find:
        item_found = True

if item_found:
    print('Item Encontrado!')
else:
    print('Item não encontrado.')

    