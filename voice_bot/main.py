from gtts import gTTS
import random
import playsound
import speech_recognition as sr

def eshit():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Gapiring!")
        audio = r.listen(source)
        print(audio)
    # recognize speech using Google Speech Recognition
    try:
        meni_gapim =  r.recognize_google(audio, language="uz")
        print("Siz: " + meni_gapim)
        return meni_gapim
    except sr.UnknownValueError:
        return "Xatolik"
    except sr.RequestError as e:
        return "Xatolik"

            #return audio
bot = "Nargiza"
yosh = 2023
def bajar(message):
    message = message.lower()
    if "salom" in message:
        gapir("Assalomu aleykum!")
    elif "nima gap" in message:
        gapir("Tinchlik")
    elif "qalay" in message:
        gapir("Raxmat yaxshi")
    elif "nargiza" in message:
        gapir("Labbay")
    elif "isming" in message:
        gapir(f"Mening ismim Nargiza")
    elif "kitob" in message:
        gapir("Sizga qanday kitoblar yoqadi?")
    elif "familiya" in message:
        gapir("Meni familiyam yo'q")
    elif "shundaymi" in message:
        gapir("Xuddi shunday")
    elif "xayr" in message:
        gapir("Dastur yakunlandi , Xayr")
        exit()
    elif "yoshim" in message:
        gapir("Tug'ilgan yilingizni ayting")
        yil = eshit()
        yosh = 2023 - int(yil)
        print(yosh)
        gapir(f"Siz {yosh} yoshdasiz")
    elif "rahmat" in message:
        gapir("Arzimaydi")
    elif "tanishamiz" in message:
        tanishuv()
    elif "xursandman" in message:
        gapir("Men ham")
    elif ""in message:
        pass
    else:
        gapir("Kechirasiz tushunmadim")

def tanishuv():
    gapir(F"Mening ismim Nargiza sizni Ismingiz nima?")
    ism = eshit()
    gapir(f"Tanishganimdan xursandman {ism}")

def gapir(message):
    ovoz = gTTS(message, lang="tr")
    fayl_nomi = "_audio_"+str(random.randint(0,100000))+".mp3"
    ovoz.save(fayl_nomi)
    playsound.playsound(fayl_nomi)
    print("Aziza: " + message)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        topshiriq = eshit()
        bajar(topshiriq)