"""
Crie um novo arquivo chamado main.py.

Importe tanto o módulo datetime quanto bday_messages (o último arquivo).

import datetime, bday_messages

Em seguida, use o módulo datetime para criar dois objetos de data:

today: A data de hoje, usando o método datetime.date.today().
next_birthday: A data do seu próximo aniversário, usando os argumentos ano, mês e dia.
Uma coisa muito legal que você pode fazer com objetos de data é adição e subtração!

time_difference = date1 - date2

Use a subtração de datas para calcular quantos dias faltam de hoje até o próximo aniversário. Em seguida, atribua o resultado a uma nova variável chamada days_away.

Depois, crie uma declaração de controle de fluxo:

Se today for igual a next_birthday, imprima a variável random_message (importada de bday_messages).
Caso contrário, imprima 'Meu próximo aniversário é daqui a {days_away} dias!'.
A saída deve ser algo assim:

Meu próximo aniversário é daqui a 42 dias!
"""

# solucao:

import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2022, 6, 26)

time_difference = next_birthday - today
days_away = time_difference.days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Meu próximo aniversário é daqui a {days_away} dias!")

    