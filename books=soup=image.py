# livros_html.py
# pip install requests beautifulsoup4
# Teste de requisição HTTP com BeautifulSoup
# Este código faz uma requisição a um site e extrai citações usando BeautifulSoup.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
 
# URL da página principal
url = "https://books.toscrape.com/"
 
# Faz a requisição
response = requests.get(url)
 
# Verifica se o request foi bem-sucedido
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    livros = soup.find_all('article', class_='product_pod')
 
    # Início do HTML
    html = '''
    <html>
    <head>
        <meta charset="utf-8">
        <title>Livros - Books to Scrape</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .livro { margin-bottom: 20px; }
            .livro img { width: 100px; height: auto; }
        </style>
    </head>
    <body>
        <h1>Livros - Books to Scrape</h1>
    '''
 
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        img_src = livro.find('img')['src']
        img_url = urljoin(url, img_src)
 
        html += f'''
        <div class="livro">
            <h2>{titulo}</h2>
            <p>Preço: {preco}</p>
            <img src="{img_url}" alt="Capa de {titulo}">
        </div>
        '''
 
    # Fim do HTML
    html += '''
    </body>
    </html>
    '''
 
    # Salva o HTML em um arquivo
    with open('books.html', 'w', encoding='utf-8') as f:
        f.write(html)
 
    print("Arquivo 'livros.html' gerado com sucesso.")
else:
    print("Erro ao acessar o site:", response.status_code)