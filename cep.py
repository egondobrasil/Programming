import requests # Biblioteca para fazer requisições HTTP.

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/' # URL da API ViaCEP com o CEP fornecido.
    response = requests.get(url) # Faz uma requisição GET para a API ViaCEP com o CEP fornecido.
    data = response.json() # Retorna a resposta da API em formato JSON.
    if 'erro' not in data:
        endereco = data['logradouro']
        bairro = data['bairro']
        cidade = data['localidade']
        estado = data['uf']
        print(f"CEP: {data['cep']}")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['uf']}")
    else:
        print("CEP não encontrado.")

cep = input("Digite o CEP (somente números): ") # Solicita ao usuário que insira o CEP.
consulta_cep(cep)