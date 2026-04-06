#pip install beautifulsoup4 requests
#beautifulsoup4: biblioteca para fazer raspagem de dados de páginas web
#requests é uma biblioteca para fazer requisições HTTP
import requests
from bs4 import BeautifulSoup


url='https://www.sp.senac.br/senac-lapa-tito/cursos-livres/curso-de-python-i-fundamentos'  # Substitua pela URL desejada
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
resp = requests.get(url, headers=headers, timeout=10)  # Fazer uma requisição GET para a URL
resp.raise_for_status()  # Verificar se a requisição foi bem-sucedida
soup = BeautifulSoup(resp.text, 'html.parser')  # Analisar o conteúdo HTML da página


#Selecionar o primeiro H1 da página
h1 = soup.select_one('h1.ssp-card-detalhe-curso__title')
print(h1.get_text(strip=True)if h1 else 'Sem H1')  # Extrair e exibir o texto do H1, ou 'Sem H1' se não houver H1 na página


h2 = soup.select_one('h2.ssp-aviso-novas-turmas__title')
print(h2.get_text(strip=True)if h2 else 'Sem tag')  # Extrair e exibir o texto da tag, ou 'Sem tag' se não houver H2 na página

span = soup.select_one('span.ssp-card-oferta-curso__valor-desconto')
print(span.get_text(strip=True)if span else 'Sem tag')  # Extrair e exibir o texto da tag, ou 'Sem tag' se ler a mesma.

h6 = soup.select_one('h6.ssp-card-oferta-curso__item-data-periodo')
print(h6.get_text(strip=True)if h6 else 'Sem tag')  # Extrair e exibir o texto da tag, ou 'Sem tag' se não houver H2 na página


p = soup.select_one('p.ssp-card-oferta-curso__dia-hora-item__dia')
print(p.get_text(strip=True)if p else 'Sem P')  # Extrair e exibir o texto do P, ou 'Sem P' se não houver P na página
#<p class="ssp-card-oferta-curso__dia-hora-item__dia"><span data-dia-hora="dias-semana">Terça a sexta: </span><span data-dia-hora="horário">13h30 às 17h30</span></p>
#<h6 class="ssp-card-oferta-curso__item-data-periodo item-data-periodo_0">10 a 13/2/2026</h6>
#<span class="ssp-card-oferta-curso__valor-desconto">R$ 300,00</span>
#<h6 class="ssp-card-oferta-curso__item-valor-investimento"><span>12x</span>R$ 50,00</h6>
#<div class="codigoOferta_9900360279 ssp-container-botao-bolsa">
# <a id="btnBolsa_0" data-index="0" class="btn btn-lg btn-info w-100 mt-3 disabled" style="font-size: 14px; font-weight: 600; background-color: rgb(0, 78, 255);" tabindex="0">Inscrições para bolsas a partir de 18/07 às 12 horas</a></div>
# select = soup.select_one('select.form-control')
# print(select.get_text(strip=True)if select else 'Sem Select')  
# <select id="unidades-ofertas" class="form-control" name="unidades-ofertas"><option value="">Clique na unidade de interesse</option><option label="Capital" disabled="disabled" class="ssp-option-group">Capital</option><option value="40404@103" data-unidade-friendly-url="senac-aclimacao" class="ssp-option">Aclimação</option><option value="40777@123" data-unidade-friendly-url="senac-francisco-matarazzo" class="ssp-option">Francisco Matarazzo</option><option value="40808@134" data-unidade-friendly-url="senac-jardim-primavera" class="ssp-option">Jardim Primavera</option><option value="40820@102" data-unidade-friendly-url="senac-lapa-tito" class="ssp-option">Lapa Tito</option><option value="40823@23" data-unidade-friendly-url="senac-largo-treze" class="ssp-option">Largo Treze</option><option value="40865@38" data-unidade-friendly-url="senac-santana" class="ssp-option">Santana</option><option value="40887@136" data-unidade-friendly-url="senac-sao-miguel-paulista" class="ssp-option">São Miguel Paulista</option><option label="Interior" disabled="disabled" class="ssp-option-group">Interior</option><option value="40756@52" data-unidade-friendly-url="senac-bauru" class="ssp-option">Bauru</option><option value="40771@54" data-unidade-friendly-url="senac-catanduva" class="ssp-option">Catanduva</option><option value="40914@73" data-unidade-friendly-url="senac-piracicaba" class="ssp-option">Piracicaba</option><option value="40890@68" data-unidade-friendly-url="senac-sao-jose-dos-campos" class="ssp-option">São José dos Campos</option><option value="40899@63" data-unidade-friendly-url="senac-taubate" class="ssp-option">Taubaté</option><option label="Grande São Paulo e Litoral" disabled="disabled" class="ssp-option-group">Grande São Paulo e Litoral</option><option value="40868@32" data-unidade-friendly-url="senac-santo-andre" class="ssp-option">Santo André</option></select>



# dropdown = soup.find("select", {"id": "dropdown_id"}) 

# if dropdown:
#     options = dropdown.find_all("option")
#     # Extract values and text
#     values = [option.get('value') for option in options]
#     texts = [option.text for option in options]
#     print(f"Option Values: {values}")
#     print(f"Option Texts: {texts}")
# else:
#     print("Dropdown not found.")

# for p in soup.select('p.ssp-card-detalhe-curso__secundary-info-carga-horaria'):
#     print(p.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo

# for div in soup.select('div.ssp-saiba-mais-curso-accordion__heading'):
#     print(div.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo

# for div in soup.select('div.ssp-saiba-mais-curso-accordion__contents'):
#     print(div.get_text(strip=True))  # Extrair e exibir o texto de cada parágrafo

