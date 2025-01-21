# Criar um programa que pede ao usuário a quantidade que ele tem em pesos, solas, e reais e calcula o total em USD.
#O resultado do programa deve ser assim:
#What do you have left in pesos? 5600
#What do you have left in soles? 105
#What do you have left in reais? 280
#413.0

# Certifique-se de pesquisar no Google as taxas de câmbio atuais!
# 1 peso vale 0,00096 usd
# 1 soles vale 0,27 usd
# 1 reais vale 0,1663 usd

# Solução:
pesos = float(input('Quanto você tem em pesos? '))
soles = float(input('Quanto você tem em soles? '))
reais = float(input('Quanto você tem em reais? '))
usd = pesos * 0.00096 + soles * 0.27 + reais * 0.1663
print('total em usd:', usd)