import tkinter as tk
from tkinter import messagebox
import requests

#Função para consultar o CEP usando a API ViaCEP
def consulta_cep(cep):
    if not cep:
        messagebox.showwarning("Atenção", "Por favor, insira um CEP válido.")
        return
    else:
        messagebox.showwarning("Erro", "CEP não encontrado.")
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
    #Fim da função

# Interface gráfica
janela = tk.Tk()
janela.title("Consulta de CEP")
janela.geometry("455x600")
janela.resizable(False, False)

#Rótulos e campos de entrada
tk.Label(janela, text="Digite o CEP")
entry_cep = tk.Entry(janela, width=30)
entry_cep.pack()


def ao_clicar():
    cep = entry_cep.get()
    consulta_cep(cep)
tk.Button(janela, text="Consultar CEP")

tk.Label(janela, text="CEP").pack(pady=3)
entry_cep = tk.Entry(janela, width=30)
entry_cep.pack()

tk.Button(janela, text="Consultar CEP", width=20, bg='#ffff00', fg='navy', command=ao_clicar).pack(pady=15)

#Rótulos com o resultado da consulta
tk.Label(janela, text="Endereço").pack(pady=3)
entry_endereco = tk.Entry(janela, width=30)
entry_endereco.pack()

tk.Label(janela, text="Número").pack(pady=3)
entry_numero = tk.Entry(janela, width=30)
entry_numero.pack()

tk.Label(janela, text="Complemento").pack(pady=3)
entry_complemento = tk.Entry(janela, width=30)
entry_complemento.pack()

tk.Label(janela, text="Bairro").pack(pady=3)
entry_bairro = tk.Entry(janela, width=30)
entry_bairro.pack()

tk.Label(janela, text="Cidade").pack(pady=3)
entry_cidade = tk.Entry(janela, width=30)
entry_cidade.pack()

tk.Label(janela, text="Estado").pack(pady=3)
entry_estado = tk.Entry(janela, width=30)
entry_estado.pack()

#Botão para gravar os dados
tk.Button(janela, text="Gravar", width=20, bg='#198754', fg='white', command='').pack(pady=15)

#Apresentando a tela:
janela.mainloop()