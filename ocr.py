# pip install pytesseract pillow

# baixe a versão portátil do tesseract em https://sourceforge.net/projects/tesseract-ocr-alt/files/
# nome do arquivo: tesseract-ocr-3.02-win32-portable.zip
# baixe o arquivo de texto em português em https://github.com/tesseract-ocr/tessdoc/blob/main/tess3/Data-Files.md
# coloque o arquivo 'por.traineddata' na pasta 'tessdata' dentro da pasta onde está o tesseract.exe

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'
Image = Image.open('imagem.jpg')

texto = pytesseract.image_to_string(Image, lang='por')

print(texto)