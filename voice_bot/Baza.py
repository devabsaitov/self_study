from main import eshit, gapir
from gtts import gTTS
import random
import playsound
import speech_recognition as sr

baza = {"salom": "Assalomu aleykum!",
        "qalesan": "Yaxshi raxmat",
        "isming": "Mening ismim Aziza"}

def Savol():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Savol: ")
        audio = r.listen(source)
        print(audio)
    # recognize speech using Google Speech Recognition
    try:
        meni_gapim = r.recognize_google(audio, language="uz")
        print("Siz: " + meni_gapim)
        return meni_gapim
    except sr.UnknownValueError:
        return "Xatolik"
    except sr.RequestError as e:
        return "Xatolik"

def Javob():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Javob: ")
        audio = r.listen(source)
        print(audio)
    # recognize speech using Google Speech Recognition
    try:
        meni_gapim = r.recognize_google(audio, language="uz")
        print("Siz: " + meni_gapim)
        return meni_gapim
    except sr.UnknownValueError:
        return "Xatolik"
    except sr.RequestError as e:
        return "Xatolik"


def urgan():
    while True:
        gapir("Baza uchun kalit so'z ayting!")
        savol = Savol()
        gapir("Endi javobni ayting")
        javob = Javob()
        gapir("Raxmat ma'lumot bazaga qo'shildi")
        baza[savol] = javob
        gapir(f"{savol} so'zi uchun javob {javob} bo'ladi ")
        if savol == "chiqish":
            exit()
urgan()