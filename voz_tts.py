# pip install gtts
# pip install playsound3
from gtts import gTTS
from playsound3 import playsound
texto = input("Digite o texto que você quer ouvir: ")
 
tts = gTTS(text=texto, lang="pt")
tts.save("vox.mp3")
playsound("vox.mp3")