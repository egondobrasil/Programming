# Instalar biblioteca
# CTRL+; faz comentário de linha
import tkinter as tk
from tkinter import messagebox
# Se o TKINTER não estivesse instalado, o nome ficaria em amarelo com um sublinhado ondulado.

#Função para calcular o IMC

#Fim de função.
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)



        if imc < 18.5: resultado = f"IMC: {imc:.2f} está abaixo do peso."
        elif 18.5 <= imc < 24.9: resultado = f"IMC: {imc:.2f} está com peso normal."
        elif 25 <= imc < 29.9: resultado = f"IMC: {imc:.2f} está com sobrepeso."
        else:resultado = f"IMC: {imc:.2f} está com obesidade."

        resultado_texto = f"Seu IMC é {imc} ({resultado})"
        label_resultado.config(text=resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")

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
label_peso.pack()

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack()
entrada_altura = tk.Entry(janela)
label_altura.pack()

# Botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)


# Iniciar a janela
janela.mainloop()