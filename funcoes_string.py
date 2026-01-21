nome = 'joão da silva'
email = 'JOAO@HOTMAIL.COM'

print(nome.upper()) # transforma todas as letras da string em maiúsculas.
print(email.lower()) # transforma todas as letras da string em minúsculas.


frase = 'bem VINDOS ao curso de Python'
print(frase.capitalize()) # transforma a primeira letra da string em maiúscula.
print(frase.title()) # transforma a primeira letra de cada palavra em maiúscula.

nome_completo = 'JOÃO ALBERTO DA SILVA'
print(nome_completo.split()) # divide a string em uma lista de palavras.

lista = ['Python', 'é', 'a', 'melhor', 'linguagem', 'de', 'programação.']
print(' '.join(lista)) # Monta uma frase a partir da lista, juntando os elementos da lista em uma única string, separados por espaço.

texto = 'Eu gosto de Java.'
print(texto.replace('Java', 'Python')) # substitui uma parte da string por outra.


nome_completo.split() # divide a string em uma lista de palavras.
nome=nome_completo.split() # atribui a lista de palavras à variável nome.
print(nome[0]) # imprime o primeiro caractere da string
print(nome[-1]) # imprime o último caractere da string

print(len(texto)) # conta o número de caracteres da string, incluindo espaços.

frase = 'Eu gosto de estudar Python.      '
posicao = frase.find(' ') # Localiza a posição do primeiro espaço em branco na string.
print(f'O espaço está na posição {posicao+1}') # Concatena a posição encontrada com uma mensagem.



#print(frase.strip()) # remove os espaços em branco do início e do fim da string.
#posicao = texto.find('Java') # procura a posição inicial da substring 'Java' na string.

