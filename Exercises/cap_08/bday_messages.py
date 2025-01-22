"""
Crie um novo arquivo chamado bday_messages.py.

Importe o módulo random.

Em seguida, defina uma lista bday_messages com os seguintes itens:

'Espero que você tenha um aniversário muito feliz! 🎈',
'É o seu dia especial – saia e comemore! 🎉',
'Você nasceu e o mundo ficou melhor – todos ganham! 🥳',
'Divirta-se muito no seu dia especial! 🎂',
'Mais um ano de você dando a volta ao sol! 🌞'
Em seguida, use o método random.choice() para obter um único item da lista.

Salve este item em uma variável chamada random_message.

Vamos salvar bday_messages.py e passar para a próxima parte.
"""

# solucao:

import random

bday_messages = [
    'Espero que você tenha um aniversário muito feliz! 🎈',
    'É o seu dia especial – saia e comemore! 🎉',
    'Você nasceu e o mundo ficou melhor – todos ganham! 🥳',
    'Divirta-se muito no seu dia especial! 🎂',
    'Mais um ano de você dando a volta ao sol! 🌞'
]

random_message = random.choice(bday_messages)
print(random_message)

