
"""
Uma máquina de jogos foi inventada no Brooklyn por volta de 1891. Os jogadores inseriam uma moeda de níquel e puxavam uma alavanca. Se fosse uma boa mão de pôquer, você ganhava uma cerveja grátis. Logo, muitos bares na cidade tinham essa máquina. Isso foi um precursor da moderna máquina caça-níqueis.

Crie um programa slot_machine.py usando o módulo random.

Os itens são símbolos de frutas comuns e setes (7️⃣). Em cada rodada, a máquina caça-níqueis exibe três itens aleatórios. Se houver três setes, você ganha!

Saída Final do Programa:

Crie uma lista de símbolos e inclua os seguintes itens: '🍒', '🍇', '🍉', '7️⃣'.

Em seguida, crie uma variável results que use o método .choices() do módulo random e obtenha três símbolos aleatórios. Certifique-se de importar o módulo necessário no topo do arquivo!

Depois, imprima cada valor de results, separado por caracteres de pipe |:

🍉 | 🍒 | 🍇

Por fim, use uma declaração if/else:

Se todos os itens da lista em results forem iguais a '7️⃣', imprima "Jackpot! 💰".
Caso contrário, imprima "Obrigado por jogar!".

"""

# solucao:

import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)

print(" | ".join(results))

if results == ['7️⃣', '7️⃣', '7️⃣']:
    print("Jackpot! 💰")
else:
    print("Obrigado por jogar!")

