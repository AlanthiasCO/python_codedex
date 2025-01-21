# Quando você vai a um drive-thru como o do McDonald's, você pode pedir comida usando os números dos itens. Por exemplo, um McLanche Feliz pode ser o #3!

# Crie um programa drive_thru.py com o menu da sua rede de fast food favorita.

# Defina uma função get_item() que receba um parâmetro, o número do item que você quer pedir, e retorne o nome desse item!

# Por exemplo, se você chamar a função com:

# Valor do argumento 1, ela pode retornar '🍔 Cheeseburger'.
# Valor do argumento 2, ela pode retornar '🍟 Batata Frita'.
# Valor do argumento 3, ela pode retornar '🥤 Refrigerante'.
# Valor do argumento 4, ela pode retornar '🍦 Sorvete'.
# Valor do argumento 5, ela pode retornar '🍪 Cookie'.
# Certifique-se de chamar essa função algumas vezes para garantir que ela funciona!

# Por fim, vamos fazer o seguinte:

# Crie um menu de boas-vindas e coloque isso em uma função welcome().
# Crie um programa principal que receba a entrada do usuário com input().

# solucionando o exercício:

def get_item(item):
    if item == 1:
        return '🍔 Cheeseburger'
    elif item == 2:
        return '🍟 Batata Frita'
    elif item == 3:
        return '🥤 Refrigerante'
    elif item == 4:
        return '🍦 Sorvete'
    elif item == 5:
        return '🍪 Cookie'
    else:
        return 'Item não encontrado!'
    
def welcome():
    print('Bem-vindo ao Drive-Thru!')
    print('Menu:')
    print('1 - 🍔 Cheeseburger')
    print('2 - 🍟 Batata Frita')
    print('3 - 🥤 Refrigerante')
    print('4 - 🍦 Sorvete')
    print('5 - 🍪 Cookie')
    print()

welcome()

item = int(input('Digite o número do item que deseja pedir: '))
print(get_item(item))
print()


