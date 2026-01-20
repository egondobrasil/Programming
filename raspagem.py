#pip install beautifulsoup4 requests
#beautifulsoup4: biblioteca para fazer raspagem de dados de páginas web
#requests é uma biblioteca para fazer requisições HTTP
import requests
from bs4 import BeautifulSoup


url='https://httpbin.org/html'  # Substitua pela URL desejada
resp = requests.get(url, timeout=10)  # Fazer uma requisição GET para a URL
resp.raise_for_status()  # Verificar se a requisição foi bem-sucedida
soup = BeautifulSoup(resp.text, 'html.parser')  # Analisar o conteúdo HTML da página


#Selecionar o primeiro H1 da página
h1 = soup.select_one('h1')
print(h1.get_text(strip=True)if h1 else 'Sem H1')  # Extrair e exibir o texto do H1, ou 'Sem H1' se não houver H1 na página

# Todos os parágrafos da página
for p in soup.select('p'):
    print(p.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo