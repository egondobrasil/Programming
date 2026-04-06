# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
 
# Url
url = "https://books.toscrape.com/"
# Fazer requisição
response = requests.get(url)
 
# Verificar se request foi bem-sucedido (Encontrou o site)
if response.status_code == 200:
    #Criar objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser'  )
    # Encontrar os livros na página
    livros = soup.find_all('article', class_='product_pod')
    # laço para ler livro a livro
    for livro in livros:
        titulo = livro.h3.a['title'] # Titulo do livro
        preco = livro.find('p', class_='price_color').text # Preço do livro
        print(f'Titulo: {titulo} | Preço: {preco}')
else:
    print("Erro ao cassar o site", response.status_code)
 