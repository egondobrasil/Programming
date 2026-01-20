#pip install PyPDF2 pyttsx3
# 
import PyPDF2 # Biblioteca para manipulação de arquivos PDF
import pyttsx3  # Biblioteca para conversão de texto em fala.


# iniciar o mecanismo de texto para fala
engine = pyttsx3.init()

#Opcional: ajustar a velocidade da fala
engine.setProperty('rate', 160)  # definir a taxa de fala
engine.setProperty('volume', 1.0)  # definir o volume (0.0 a 1.0)

#Abrir o arquivo PDF
with open(r'C:\Users\egon.wvwitte\OneDrive - SENAC - SP\Python\Programming\AF_EM-CARTAZ_JAN_2026_BAIXA.pdf', 'rb') as texto_pdf:
    leitor = PyPDF2.PdfReader(texto_pdf)
    numero_de_paginas = len(leitor.pages)

    #Ler/Iterar por todas as páginas do PDF
    for pagina in leitor.pages:
        texto = pagina.extract_text()
        if texto:
            print(texto)  # Exibir o texto extraído no console
            engine.say(texto)  # Converter o texto em fala

#Executar a fala
engine.runAndWait()