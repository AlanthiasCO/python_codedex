"""
É hora de abrir uma conta bancária! 🏦

Crie um arquivo chamado bank_accounts.py.

Vamos definir uma classe BankAccount. Em seguida, vamos usar o método __init__() para definir os seguintes atributos:

first_name (string)
last_name (string)
account_id (inteiro)
account_type (string)
pin (inteiro)
balance (float)
Em seguida, vamos criar três métodos:

.deposit(): Adicionar dinheiro na conta e retornar o novo saldo.
.withdraw(): Retirar dinheiro subtraindo do saldo e retornando o valor retirado.
.display_balance(): Imprimir o valor atual do saldo.
Por fim, inicialize um novo objeto da classe BankAccount e use esses métodos para fazer o seguinte:

Depositar $96 na conta.
Retirar $25 da conta.
Imprimir o saldo atual da conta.
"""

# solucao:

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return amount
    
    def display_balance(self):
        print(f"Seu saldo atual é: ${self.balance}")

#Inicializar um novo objeto da classe BankAccount.
account = BankAccount("John", "Doe", 123456, "Conta Corrente", 1234, 0)

#Depositar $96 na conta.
account.deposit(96)


#Retirar $25 da conta.
account.withdraw(25)

#Imprimir o saldo atual da conta.
account.display_balance()