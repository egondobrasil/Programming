from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("https://www.sp.senac.br/senac-lapa-tito/cursos-livres/curso-de-python-i-fundamentos", headers={'User-Agent': 'Mozilla/5.0'}) # type: ignore
webpage = urlopen(req).read() # type: ignore

# Parsing html with BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")



#Selecionar o primeiro H1 da página
h1 = soup.select_one('h1.ssp-card-detalhe-curso__title')
print(h1.get_text(strip=True)if h1 else 'Sem H1')  # Extrair e exibir o texto do H1, ou 'Sem H1' se não houver H1 na página

# Todos os parágrafos da página
for p in soup.select('p.ssp-card-detalhe-curso__secundary-info-carga-horaria'):
    print(p.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo


h6 = soup.select_one('h6.ssp-card-oferta-curso__item-valor-investimento')
print(h6.get_text(strip=True)if h6 else 'Sem H6')  # Extrair e exibir o texto do H6, ou 'Sem H6' se não houver H6 na página