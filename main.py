import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import LolAPI

r = sr.Recognizer()

def siteleriAc():
    webbrowser.get().open("https://www.facebook.com")
    webbrowser.get().open("https://www.youtube.com")
    webbrowser.get().open("https://outlook.live.com/mail/0/inbox")
    webbrowser.get().open("https://mail.google.com/mail/u/0/#inbox")
    webbrowser.get().open("https://mail.gop.edu.tr/mail/")

def konus(cumle):
    tts = gTTS(cumle, lang="tr")
    x = random.randint(0, 500000000)
    dosya = "ses-" + str(x) + ".mp3"
    tts.save(dosya)
    playsound(dosya)
    os.remove(dosya)

def hafiftenDinle():
    with sr.Microphone() as source:
        dinle = r.listen(source)
        ses = ""
        try:
            ses = r.recognize_google(dinle, language='tr-TR')
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except Exception:
            pass
        print(ses)
        return ses

def kaydet(soru=""):
    with sr.Microphone() as source:
        if not soru == "":
            konus(soru)
        dinle = r.listen(source)
        ses = ""
        try:
            ses = r.recognize_google(dinle, language='tr-TR')
        except sr.UnknownValueError:
            konus("Başaramadık beyim")
        except sr.RequestError:
            konus("Sistemde sorun var beyim")
        except Exception:
            konus("Beyim yardım")
        print(ses)
        return ses

def cevap(kayit):
    if "aleykümselam" in kayit.lower():
        konus("Eyvallah beyim.")
    elif "vakit" in kayit.lower():
        konus("Vakit imdi" + datetime.now().strftime('%H:%M:%S') + " vaktidir beyim")
    elif "lol" in kayit.lower():
        lolBilgisi()
    elif "ara" in kayit.lower():
        search = kaydet("Ne istersiniz beyim.")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        konus("Buyur beyim.")
    elif "çemen" in kayit.lower():
        konus("Pusatın keskin, yolun açık olsun beyim.")
        exit()
    elif "uyu" in kayit.lower():
        konus("Vakit imdi nöbet vaktidir beyim.")
        while True:
            kayitt = hafiftenDinle()
            if "uyan" in kayitt.lower():
                konus("Allahuekber")
                return
    elif "siteleri aç" in kayit.lower():
        siteleriAc()
        konus("Buyur beyim.")
    else:
        konus("Sen ne dersin beyim")


"""def erisimKontrolu(ses):
    if "bacı" in ses.lower():
        return True
    else:
        return False"""

def lolBilgisi():
    koridor = input(konus("Koridor söyle beyim"))
    if "üst" in koridor.lower() or "top" in koridor.lower():
        koridor = "Top"
    elif "orta" in koridor.lower() or "mid" in koridor.lower():
        koridor = "Middle"
    elif "orman" in koridor.lower():
        koridor = "Jungle"
    elif "nişancı" in koridor.lower():
        koridor = "ADC"
    elif "destek" in koridor.lower() or "sup" in koridor.lower():
        koridor = "Support"
    else:
        konus("Error beyim")
        return

    konus("Şampiyon söyle beyim")
    sampiyon = input()
    konus("Peki ya sen ne istersin beyim?")
    istek = input()

    if "rün" in istek.lower() and "kazan" in istek.lower():
        konus(LolAPI.runBilgisi(sampiyon=sampiyon,rol=koridor,tercih=False))
    elif "rün" in istek.lower():
        konus(LolAPI.runBilgisi(sampiyon=sampiyon,rol=koridor))
    elif "bilgi" in istek.lower():
        konus("ilerde olur inşallah beyim")
    else:
        konus("Anlamadım beyim")

def main():
    konus("Hoşgeldiniz beyim")
    while True:
        cevap(str(input("gir")))

main()