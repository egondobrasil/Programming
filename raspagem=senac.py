#pip install beautifulsoup4 requests
#beautifulsoup4: biblioteca para fazer raspagem de dados de páginas web
#requests é uma biblioteca para fazer requisições HTTP
import requests
from bs4 import BeautifulSoup


url='https://www.sp.senac.br/senac-lapa-tito/cursos-livres/curso-de-python-i-fundamentos'  # Substitua pela URL desejada
resp = requests.get(url, timeout=10)  # Fazer uma requisição GET para a URL
resp.raise_for_status()  # Verificar se a requisição foi bem-sucedida
soup = BeautifulSoup(resp.text, 'html.parser')  # Analisar o conteúdo HTML da página


#Selecionar o primeiro H1 da página
h1 = soup.select_one('h1.ssp-card-detalhe-curso__title')
print(h1.get_text(strip=True)if h1 else 'Sem H1')  # Extrair e exibir o texto do H1, ou 'Sem H1' se não houver H1 na página

# Todos os parágrafos da página
for p in soup.select('p.ssp-card-detalhe-curso__secundary-info-carga-horaria'):
    print(p.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo


h6 = soup.select_one('h6.ssp-card-oferta-curso__item-valor-investimento')
print(h6.get_text(strip=True)if h6 else 'Sem H6')  # Extrair e exibir o texto do H6, ou 'Sem H6' se não houver H6 na página