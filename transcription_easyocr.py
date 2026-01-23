import easyocr
 
reader = easyocr.Reader(['ar']) # idioma do texto
 
# paragraph=True: tenta agrupar linhas próximas em blocos de texto
# contrast_ths: ajusta a sensibilidade ao contraste
resultado = reader.readtext('Zimplified_Arabic.png', detail=0, paragraph=True)
 
print(resultado)