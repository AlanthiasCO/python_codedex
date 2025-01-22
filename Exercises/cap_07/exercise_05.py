"""
Instruções:
Crie um novo arquivo chamado pokedex.py.

Em seguida, vamos definir uma classe Pokemon com os seguintes atributos:

entry (inteiro)
name (string)
types (lista de strings)
description (string)
is_caught (booleano)
Nota: Certifique-se de usar o método __init__().

Em seguida, crie um método de instância chamado .speak() que imprime uma string do som que um Pokémon faz. Um Pokémon geralmente apenas diz seu nome, então faça o .speak() simplesmente imprimir o nome duas vezes!

Depois, crie outro método de instância chamado .display_details() que imprime os atributos de um objeto Pokemon como o seguinte:

Número de Entrada: 25
Nome: Pikachu
Tipo: Elétrico
Descrição: Ele tem pequenos sacos elétricos em ambas as bochechas. Se ameaçado, ele libera cargas elétricas dos sacos.
Pikachu já foi capturado!

Por fim, crie três objetos da classe Pokemon e use os métodos de instância .speak() ou .display_details() para cada um.

Para mais informações sobre qualquer Pokémon que você queira adicionar, consulte o Pokédex!

Você está pronto para ganhar a próxima insígnia?

Bônus: Para todos os super fãs, tente adicionar mais atributos à definição da classe Pokemon, como nível, região, altura ou peso.

"""

# solucao:

class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(f"{self.name}! {self.name}!")
    
    def display_details(self):
        print(f"Número de Entrada: {self.entry}")
        print(f"Nome: {self.name}")
        print(f"Tipo: {', '.join(self.types)}")
        print(f"Descrição: {self.description}")
        if self.is_caught:
            print(f"{self.name} já foi capturado!")
        else:
            print(f"{self.name} ainda não foi capturado!")

pikachu = Pokemon(25, "Pikachu", ["Elétrico"], "Ele tem pequenos sacos elétricos em ambas as bochechas. Se ameaçado, ele libera cargas elétricas dos sacos.", True)
bulbasaur = Pokemon(1, "Bulbasaur", ["Grama", "Veneno"], "Bulbasaur pode ser visto cochilando sob a luz do sol. Há uma semente em suas costas. Ao absorver a luz do sol, a semente cresce progressivamente.", False)
charmander = Pokemon(4, "Charmander", ["Fogo"], "A chama que arde na ponta da cauda de Charmander indica sua saúde e emoções. Se a chama diminuir, Charmander está doente.", False)

pikachu.speak()
pikachu.display_details()
bulbasaur.speak()
bulbasaur.display_details()
charmander.speak()
charmander.display_details()

