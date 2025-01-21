# Vamos começar um clube do livro fazendo uma lista de livros populares! 📚

# Criar um programa lendo_list.py que armazena os seguintes itens em uma lista books:

# 'Harry Potter'
# '1984'
# 'The Fault in Our Stars'
# 'The Mom Test'
# 'Life in Code'

# Suponha que queremos adicionar 'Pachinko' à lista. Você pode usar um método de lista para fazer isso?

# Digamos que terminamos de ler 'The Fault in Our Stars' e '1984'. Você pode usar o método .remove() para remover um
#  e o método .pop() para remover o outro?

# Imprima a lista atualizada para garantir que tudo está certo!

# Solucao:

book_list = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']
print(book_list) # Imprime a lista de livros
book_list.append('Pachinko') # Adiciona 'Pachinko' à lista
book_list.remove('The Fault in Our Stars') # Remove 'The Fault in Our Stars' da lista
book_list.pop(1) # Remove '1984' da lista
print(book_list) # Imprime a lista atualizada
