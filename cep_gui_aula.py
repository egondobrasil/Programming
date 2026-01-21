#cep_grafico.py
import tkinter as tk
from tkinter import messagebox
import requests
 
# Função de  consulta de cep
def consultar_cep():
    cep = entry_cep.get().strip()
    if not cep:
        messagebox.showwarning("Atenção", "Digite um Cep.")
        return
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()  
 
    if "erro" not in data:
        entry_endereco.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
        entry_estado.delete(0, tk.END)
 
        entry_endereco.insert(0, data["logradouro"])
        entry_bairro.insert(0, data["bairro"])
        entry_cidade.insert(0, data["localidade"])
        entry_estado.insert(0, data["uf"])
   
    else:
        messagebox.showwarning("Erro", "Cep não Encontrado.")
# Fim da função
 
# Interface gráfica
janela = tk.Tk()
janela.title("Consulta do Cep")
janela.geometry("210x480")
janela.resizable(False,False)
 
# Labels e entrys
tk.Label(janela, text="CEP").pack(pady=3)
entry_cep = tk.Entry(janela, width=9)
entry_cep.pack()
 
tk.Button(janela, text="Consultar CEP", command=consultar_cep,width=20,bg="#ffff00",fg="navy").pack(pady=8)
 
 
tk.Label(janela, text="Endereço").pack(pady=3)
entry_endereco = tk.Entry(janela, width=32)
entry_endereco.pack()
 
tk.Label(janela, text="Número").pack(pady=3)
entry_numero = tk.Entry(janela, width=5)
entry_numero.pack()
 
tk.Label(janela, text="Complemento").pack(pady=3)
entry_complemento = tk.Entry(janela, width=5)
entry_complemento.pack()
 
tk.Label(janela, text="Bairro").pack(pady=3)
entry_bairro = tk.Entry(janela, width=30)
entry_bairro.pack()
 
tk.Label(janela, text="Cidade").pack(pady=3)
entry_cidade = tk.Entry(janela, width=15)
entry_cidade.pack()
 
tk.Label(janela, text="Estado").pack(pady=3)
entry_estado = tk.Entry(janela, width=3)
entry_estado.pack()
 
 
#Botão gravar
tk.Button(janela,text="Gravar",width=20,bg="#198754",fg="white").pack(pady=15)

#Botão Copiar
tk.Button(janela,text="Copiar",width=20,bg="navy",fg="white").pack(pady=15)

# Apresentando a tela
janela.mainloop()