#Coleção de dados organizados em uma única variável.

#Lista vazia
nomes = []

#Lista com elementos
nomes = ['Ana', 'Marcelo', 'Ricardo', 'Bernardo', 'Alexandre']
print(nomes)

print(nomes[0]) #Acessa o primeiro elemento da lista
print(nomes[4]) #Acessa o quinto elemento da lista
nomes.append('Raimundo') #Adiciona um elemento ao final da lista
print(nomes)
nomes.insert(2, 'Thais') #Adiciona um elemento na posição desejada
print(nomes)
nomes.extend(['Sérgio', 'Maria','Antônio']) #Adiciona vários elementos ao final da lista
print(nomes)


#Alterar o valor de deternada posição
nomes[0] = 'Alice'
print(nomes)

nomes.remove('Maria') #Remove o elemento pelo valor
print(nomes)

del nomes[1] #Remove o elemento pela posição
print(nomes)

ultimo_nome = nomes.pop() #Remove o último elemento e retorna o valor removido
print(ultimo_nome)
print(nomes)

#nomes.clear() #Remove todos os elementos da lista
print(nomes)

print('Marcelo' in nomes) #Verifica se o elemento está na lista, retorna True ou False
print("Alice" in nomes) #Verifica se o elemento está na lista, retorna True ou False



#Contar ocorrências de um elemento na lista
nomes.append('Alice') #Adiciona um elemento ao final da lista
print(nomes.count('Alice'))

nomes.sort() #Ordena a lista em ordem alfabética
print(nomes)

nomes.sort(reverse=True) #Ordena a lista em ordem alfabética reversa
#nomes.reverse() #Inverte a ordem da lista
print(nomes)



#---------------------------------------------------------------------------------------------------------------
#Tuplas: Também são uma coleção de dados, porém são imutáveis, ou seja, não podem ser alteradas após a criação.
veiculos = ()
print(veiculos)
veiculos = ('Toyota', 'Nissan', 'Renault', 'Volkswagen')
print(veiculos)


#Tupla mista
Cadastro = ('Ana', 25, 1800.25, True)
print(Cadastro)
print(Cadastro[1]) #Acessa o primeiro elemento da tupla

#---------------------------------------------------------------------------------------------------------------
#Dicionários: Coleção de dados que armazenam pares de chave-valor.
#O dicionário é uma estrutura mutável que armazena chave e valor. Era imutável até a versão 3.6 do Python. As chaves são únicas, não pode haver outra com mesmo nome.

pessoa = {'Nome': 'Ana Maria', 'idade': 25, 'salario': 1850.30, 'matriculada': True}
print(pessoa)
print(pessoa['Nome']) #Acessa o valor da chave 'Nome'
print(pessoa['idade']) #Acessa o valor da chave 'idade'
pessoa['Celular'] = ("(11) 99888-7755") #Altera o valor da chave 'idade'
print(pessoa)
pessoa['idade'] = 26 #Altera o valor da chave 'idade', sobrescrevendo o valor antigo
print(pessoa)
pessoa['peso'] = 60 #Adiciona uma nova chave 'peso' com o valor 60
print(pessoa)
del pessoa['peso'] #Remove a chave 'peso' e seu valor
print(pessoa)

#pessoa.clear() #Remove todos os elementos do dicionário
print(pessoa.keys()) #Retorna todas as chaves do dicionário
print(pessoa.values()) #Retorna todos os valores do dicionário

for chave, valor in pessoa.items(): #Percorre o dicionário exibindo chave e valor
    #print(f"{chave}: {valor}")
    print(chave, "=", valor)


#---------------------------------------------------------------------------------------------------------------
#Lista: [], Mutável, Ordenada, Acesso: Índice Numérico.
#Tupla: (), Imutável, Ordenada, Acesso: Índice Numérico.
#Dicionário: {}, Mutável, Não Ordenada, Pares chave-valor, Acesso: Chave-Valor.