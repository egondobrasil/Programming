import pandas as pd

dados = [
    {"nome": "Ana",   "cidade": "São Paulo", "idade": 21, "curso": "Python", "nota": 8.5},
    {"nome": "Bruno", "cidade": "Osasco",    "idade": 19, "curso": "Python", "nota": 7.0},
    {"nome": "Carla", "cidade": "São Paulo", "idade": 22, "curso": "Web",    "nota": 9.2},
    {"nome": "Diego", "cidade": "Barueri",   "idade": 18, "curso": "Web",    "nota": 6.8},
    {"nome": "Eva",   "cidade": "Osasco",    "idade": 20, "curso": "Python", "nota": 9.0},
]

df = pd.DataFrame(dados)
print(df) #Postra a tabela
print('------------------------------------------------')
print(df.head(3)) # Mostra os primeiros 3 registros
print('------------------------------------------------')
print(df.info()) # Mostra tipos e nulos
print('------------------------------------------------')
print(df.describe())# Mostra estatísticas numéricas
print('------------------------------------------------')


#Seleção de colunas e linhas
#Coluna única
print(df['nome'])
print('------------------------------------------------')
# Várias Colunas
print(df[['nome','curso','nota']])
print('------------------------------------------------')
# Linha por índice
print(df.loc[2]) # Mostra a linha do índice 2
print('------------------------------------------------')
# Fatiamento
print(df.loc[1:3]) # Mostra as linhas 1 a 3, que seriam da segunda a quarta coluna.
print('------------------------------------------------')
# Filtrando dados
#Alunos de Python
print(df[df['curso']=='Python'])


print('------------------------------------------------')
print(df[df['nota']>=8])


print('------------------------------------------------')
# Combinações e condições
filtro = (df["curso"] == "Python") & (df["nota"]>=8)
print(filtro)
print('------------------------------------------------')
#Ordenar e contar
#Ordenação decrescente
print(df.sort_values(by='nota',ascending=False))

print('------------------------------------------------')
# Contar valores de uma coluna
print(df['cidade'].value_counts())

print('------------------------------------------------')
# Criar coluna nova
df['aprovado'] = df['nota']>=7
df['faixa'] = df['nota'].apply(lambda x:'Excelente' if x>=9 else ('Boa' if x>=7 else 'reforço'))
print(df)

print('------------------------------------------------')
# Agrupamento (group by do SQL)
# Pergunta: Média por curso
print(df.groupby('curso')['nota'].mean())
print(df.groupby('curso')['nota'].sum())


print('------------------------------------------------')
# Exportar CSV
#df.to_csv('alunos.csv',index=False,encoding='utf-8')


# Ler CSV:
print('Leitura do arquivo CSV:')
df2 = pd.read_csv('alunos.csv')
print(df2)

print('------------------------------------------------')
print('Deus é fiel:')
deusehfiel = pd.DataFrame(dados)
print(deusehfiel.groupby('curso')['nota'].mean())