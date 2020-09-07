import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import requests
from bs4 import BeautifulSoup

r = sr.Recognizer()

def runGoster(sampiyon, rol):
    sayfa = requests.get('https://champion.gg/champion/' + sampiyon + '/' + rol)
    soup = BeautifulSoup(sayfa.content, 'html.parser')
    ilkSayfaVerileri = soup.find_all('div', {"class": "Description__Title-jfHpQH bJtdXG"})
    ikinciSayfaVerileri = soup.find_all('div', {'class': 'Description__Title-jfHpQH eOLOWg'})
    baslikVerileri = soup.find_all('div',
                                   {'class': 'KeyStoneSlot__Title-krZhKQ eQgjEC Description__Title-jfHpQH bJtdXG'})
    baslik = []
    birinciSayfa = []
    ikinciSayfa = []
    kazandiran = []
    secilen = []
    for i in ilkSayfaVerileri:
        birinciSayfa.append(i.text)
    for i in ikinciSayfaVerileri:
        ikinciSayfa.append(i.text)
    for i in baslikVerileri:
        baslik.append(i.text)

    kazandiran.append(baslik[0])  # En çok kazandıran
    for i in range(4):
        kazandiran.append(birinciSayfa[i])
    for i in range(3):
        kazandiran.append(ikinciSayfa[i])
    for i in range(4, 7):
        kazandiran.append(birinciSayfa[i])

    secilen.append(baslik[1])  # En çok tercih edilen
    for i in range(7, 11):
        secilen.append(birinciSayfa[i])
    for i in range(3, 6):
        secilen.append(ikinciSayfa[i])
    for i in range(11, 14):
        secilen.append(birinciSayfa[i])


    if secilen[0] == "Precision":
        secilen[0] = "İsabet"

        if secilen[1].lower() == "conqueror":
            secilen[1] = "Yenilmez"
        elif secilen[1].lower == "fleet footwork":
            secilen[1] = "Ayağı Çabuk"
        elif secilen[1].lower == "lethal tempo":
            secilen[1] = "Ölümcül Tempo"
        elif secilen[1].lower == "press the attack":
            secilen[1] = "Saldırıya Devam"


    elif secilen[0] == "Domination":
        secilen[0] = "Hakimiyet"
    elif secilen[0]== "Sorcery":
        secilen.insert("Büyücülük",0)
    elif secilen[0] == "Resolve":
        secilen[0] = "Azim"
    elif secilen[0] == "Inspiration":
        secilen[0] = "İlham"

    secilenString = "En çok seçilen sayfası "
    for i in secilen:
        secilenString += i + " "
    return secilenString


def siteleriAc():
    webbrowser.get().open("https://www.facebook.com")
    webbrowser.get().open("https://www.youtube.com")
    webbrowser.get().open("https://outlook.live.com/mail/0/inbox")
    webbrowser.get().open("https://mail.google.com/mail/u/0/#inbox")
    webbrowser.get().open("https://mail.gop.edu.tr/mail/")

def konus(cumle):
    tts = gTTS(cumle, lang="tr")
    x = random.randint(0,50000)
    dosya = "ses-"+str(x)+".mp3"
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

def kaydet(soru = ""):
     with sr.Microphone() as source:
        if not soru == "":
            konus(soru)
        dinle = r.listen(source)
        ses=""
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
        konus(datetime.now().strftime('%H:%M:%S'))
    elif "jax" in kayit.lower() and "top" in kayit.lower():
        konus(runGoster(sampiyon="jax", rol="top"))
    elif "ara" in kayit.lower():
        search = kaydet("Ne istersiniz beyim.")
        url = "https://google.com/search?q="+search
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

def main():
    konus("Hoşgeldiniz beyim")
    time.sleep(1)
    while True:
        cevap(str(input("gir")))

main()