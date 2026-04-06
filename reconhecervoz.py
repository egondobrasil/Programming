import speech_recognition as sr
from gtts import gTTS
from playsound3 import playsound
 
# iniciar o reconhecedor
reconhecedor = sr.Recognizer()
 
print("Fale alguma coisa...")
 
with sr.Microphone() as fonte:
    reconhecedor.adjust_for_ambient_noise(fonte, duration=1)
    audio = reconhecedor.listen(fonte)
 
try:
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print("Você disse: ", texto)
    #Converter voz em texto
 
except sr.UnknownValueError:
    print("Não entendi")
except sr.RequestError as e:
    print("Erro no serviço de reconhecimento: {e}")