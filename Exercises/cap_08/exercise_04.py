"""
É hora de experimentar um pacote Python!

Primeiro, certifique-se de que o pip está instalado executando pip3 em um terminal. Se não estiver, siga os passos para instalá-lo aqui.

Em seguida, instale um pacote chamado wikipedia.

pip3 install wikipedia

Depois, crie um novo arquivo chamado wiki.py.

Então, use a documentação do pacote wikipedia para pesquisar uma frase de sua escolha.

Alguns exemplos poderiam ser:

"Filosofia de vida"
"Python (linguagem de programação)"
"Galáxia"
Tente executar este programa no terminal com:

python3 wiki.py

"""

# solucao:

import wikipedia

search = input("Enter a search term: ")
result = wikipedia.summary(search, sentences=2)
print(result)

