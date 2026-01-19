# Instalar biblioteca
# CTRL+; faz comentário de linha
import tkinter as tk
from tkinter import messagebox
# Se o TKINTER não estivesse instalado, o nome ficaria em amarelo com um sublinhado ondulado.

#Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        if imc < 18.5:
            resultado = f"IMC: {imc:.2f} - Abaixo do peso"
        elif imc < 24.9:
            resultado = f"IMC: {imc:.2f} - Peso Normal"
        elif imc < 29.9:
            resultado = f"IMC: {imc:.2f} - Sobre peso"
        elif imc < 34.9:
            resultado = f"IMC: {imc:.2f} - Obesidade grau I"
        elif imc < 39.9:
            resultado = f"IMC: {imc:.2f} - Obesidade grau II"
        else:
            resultado = f"IMC: {imc:.2f} - Obesidade grau III Morbida"
 
        # Exibir Resultado
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos")
 
# Fim da função
#Configura a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("600x500")
janela.resizable(False, False)



# Labels e Entradas
label_titulo = tk.Label(janela, text="Calculadora de IMC", font=("Arial", 14, "bold")) # Título em negrito
label_titulo.pack(pady=10) # Espaçamento entre as linhas de 10px
# Labels e Entradas
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()

# Botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)


# Iniciar a janela
janela.mainloop()