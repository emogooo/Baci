import requests
from googletrans import Translator
from bs4 import BeautifulSoup
trans = Translator()
sampiyon = "JarvanIV"
rol = "Jungle"
sayfa =requests.get('https://champion.gg/champion/' + sampiyon + '/' + rol)
soup = BeautifulSoup(sayfa.content, 'html.parser')
ilkSayfaVerileri = soup.find_all('div',{"class":"Description__Title-jfHpQH bJtdXG"})
ikinciSayfaVerileri = soup.find_all('div', {'class':'Description__Title-jfHpQH eOLOWg'})
baslikVerileri = soup.find_all('div', {'class':'KeyStoneSlot__Title-krZhKQ eQgjEC Description__Title-jfHpQH bJtdXG'})
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

kazandiran.append(baslik[0])    #En çok kazandıran
for i in range(4):
    kazandiran.append(birinciSayfa[i])
for i in range(3):
    kazandiran.append(ikinciSayfa[i])
for i in range(4,7):
    kazandiran.append(birinciSayfa[i])

secilen.append(baslik[1])    #En çok tercih edilen
for i in range(7,11):
    secilen.append(birinciSayfa[i])
for i in range(3,6):
    secilen.append(ikinciSayfa[i])
for i in range(11,14):
    secilen.append(birinciSayfa[i])


print("En çok tercih edilen:")
for i in secilen:
    print(i)
print("\nEn çok kazandıran:")
for i in kazandiran:
    print(i)

if secilen[0].lower == "precision":
    secilen[0] = "İsabet"
elif secilen[0].lower == "domination":
    secilen[0] = "Hakimiyet"
elif secilen[0].lower == "sorcery":
    secilen[0] = "Büyücülük"
elif secilen[0].lower == "resolve":
    secilen[0] = "Azim"
elif secilen[0].lower == "inspiration":
    secilen[0] = "İlham"