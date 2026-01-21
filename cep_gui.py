import tkinter as tk
from tkinter import messagebox
import requests

#Função para consultar o CEP usando a API ViaCEP
def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    data = response.json()
    if 'erro' not in data:
        endereco = data['logradouro']
        bairro = data['bairro']
        cidade = data['localidade']
        estado = data['uf']
        resultado = (f"CEP: {data['cep']}\n"
                     f"Logradouro: {data['logradouro']}\n"
                     f"Bairro: {data['bairro']}\n"
                     f"Cidade: {data['localidade']}\n"
                     f"Estado: {data['uf']}")
        messagebox.showinfo("Resultado da Consulta", resultado)
    else:
        messagebox.showerror("Erro", "CEP não encontrado.")
#Fim da função

# Interface gráfica
janela = tk.Tk()
janela.title("Consulta de CEP")
janela.geometry("255x120")
janela.resizable(False, False)
label = tk.Label(janela, text="Digite o CEP (somente números):")
label.pack(pady=10)
entrada_cep = tk.Entry(janela)
entrada_cep.pack(pady=5)
def ao_clicar():
    cep = entrada_cep.get()
    consulta_cep(cep)
botao_consultar = tk.Button(janela, text="Consultar", command=ao_clicar)
botao_consultar.pack(pady=10)   

#Apresentando a tela:
janela.mainloop()