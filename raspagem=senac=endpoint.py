#pip install requests
import requests
import json

# API endpoint for course details
api_url = 'https://www.sp.senac.br/o/senac-content-services/cursosInfoDetalhe/20125/31899361'

params = {
    'inscricaoAberta': 'false',
    'bolsaAberta': 'false',
    'buscarUnidadesComOferta': 'true'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

try:
    resp = requests.get(api_url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    
    data = resp.json()
    print(json.dumps(data, indent=2))  # Print to see the structure
    
    # Now extract the scholarship data you need
    if 'ofertas' in data:
        for oferta in data['ofertas']:
            if 'dataAberturaBolsaOferta' in oferta and 'horaAberturaBolsaOferta' in oferta:
                data_abertura = oferta['dataAberturaBolsaOferta']
                hora_abertura = oferta['horaAberturaBolsaOferta']
                
                # Format the text like the button
                textoBotaoBolsa = f"Inscrições para bolsas a partir de {formataDataAberturaBolsa(data_abertura, hora_abertura)}"
                print(textoBotaoBolsa)
                
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")