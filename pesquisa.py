import speech_recognition as sr
import pyaudio
import os 

def ouvir_Mic():

    mic = sr.Recognizer()

    with sr.Microphone() as source:

        mic.adjust_for_ambient_noise(source)
        print("Diga algo para pesquisar: ")
        audio = mic.listen(source)

    try:

        frase = mic.recognize_google(audio, language='pt-BR')
        os.system("start " + "https://www.google.com/search?q=" + frase)
        print("frase: " + frase)

    except sr.UnknownValueError: 
        print("erro")

ouvir_Mic()