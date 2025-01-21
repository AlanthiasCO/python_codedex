# No setor de fintech, frequentemente realizamos uma análise de séries temporais em ações. Isso significa que precisamos analisar uma ação, dado seu preço ao longo de um certo período. 📈

# Neste exercício, realizaremos uma versão simplificada de uma análise de séries temporais. A ação que analisaremos é a ação $AMC em janeiro de 2023.

# Aqui estão os preços das ações (em dólares) para cada um desses dias úteis:

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

# Crie um programa stock_analysis.py que implemente três funções:

# price_at(x) que encontra o preço em um determinado dia x.
# max_price(a, b) que encontra o preço máximo do dia a ao dia b.
# min_price(a, b) que encontra o preço mínimo do dia a ao dia b.
# Os parâmetros dos dias estarão no intervalo de 1 a 20 (já que esse é o período para a ação que estamos analisando).

# Certifique-se de chamar cada função para testar se suas funções funcionam corretamente!

# solucao:

def price_at(x):
    return stock_prices[x - 1]

def max_price(a, b):
    return max(stock_prices[a - 1:b])

def min_price(a, b):
    return min(stock_prices[a - 1:b])

#or
""""
def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn
"""

print(price_at(1))
print(max_price(1, 5))
print(min_price(1, 5))
# Output:
# 34.68
# 36.09
# 33.97
