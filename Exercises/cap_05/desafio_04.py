# Aqui está uma lista de preços em Python para o que foi pedido:
# bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
# Usando esta lista bill, calcule o valor total e depois divida-o em quatro partes.
# Inicialize o total com zero e percorra a lista bill para somar tudo.
# 
# Com o total, armazene o que cada pessoa deve pagar em uma variável my_share e depois imprima o resultado no terminal.

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0
my_share = 0

for item in bill:
    total += item

my_share = total / 4

print(f'O valor total da conta é: R${total:.2f}')  # usando .2f para formatar o float com duas casas decimais  
print(f'Cada pessoa deve pagar: R${my_share:.2f}')

