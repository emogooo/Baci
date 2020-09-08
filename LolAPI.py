import requests
from bs4 import BeautifulSoup

def runBilgisi(sampiyon, rol = "Top", tercih = True):
    sayfa = requests.get("https://champion.gg/champion/" + sampiyon + "/" + rol)
    soup = BeautifulSoup(sayfa.content, "html.parser")
    ilkSayfaVerileri = soup.find_all(
        "div", {"class": "Description__Title-jfHpQH bJtdXG"}
    )
    ikinciSayfaVerileri = soup.find_all(
        "div", {"class": "Description__Title-jfHpQH eOLOWg"}
    )
    baslikVerileri = soup.find_all(
        "div",
        {"class": "KeyStoneSlot__Title-krZhKQ eQgjEC Description__Title-jfHpQH bJtdXG"},
    )

    baslik = []
    birinciSayfa = []
    ikinciSayfa = []

    for i in ilkSayfaVerileri:
        birinciSayfa.append(i.text)
    for i in ikinciSayfaVerileri:
        ikinciSayfa.append(i.text)
    for i in baslikVerileri:
        baslik.append(i.text)

    if tercih:
        secilen = []
        secilen.append(baslik[1])  # En çok tercih edilen
        for i in range(7, 11):
            secilen.append(birinciSayfa[i])
        for i in range(3, 6):
            secilen.append(ikinciSayfa[i])
        for i in range(11, 14):
            secilen.append(birinciSayfa[i])
        secilen = turkceyeCevir(secilen)
        secilenString = "En çok seçilen: "
        for i in secilen:
            secilenString += i + " - "
        secilenString = secilenString[:(secilenString.__len__() - 2)]
        return secilenString

    else:
        kazandiran = []
        kazandiran.append(baslik[0])  # En çok kazandıran
        for i in range(4):
            kazandiran.append(birinciSayfa[i])
        for i in range(3):
            kazandiran.append(ikinciSayfa[i])
        for i in range(4, 7):
            kazandiran.append(birinciSayfa[i])
        kazandiran = turkceyeCevir(kazandiran)
        kazandiranString = "En çok kazandıran: "
        for i in kazandiran:
            kazandiranString += i + " - "
        kazandiranString = kazandiranString[:kazandiranString.__len__() - 2]
        return kazandiranString

def turkceyeCevir(dizi):
    if dizi[0].lower() == "precision":
        dizi[0] = "İsabet"
        dizi = isabetBirincil(dizi)
        if dizi[5].lower() == "resolve":
            dizi[5] = "Azim"
            dizi = azimIkincil(dizi)
        elif dizi[5].lower() == "sorcery":
            dizi[5] = "Büyücülük"
            dizi = buyuculukIkincil(dizi)
        elif dizi[5].lower() == "domination":
            dizi[5] = "Hakimiyet"
            dizi = hakimiyetIkincil(dizi)
        elif dizi[5].lower() == "inspiration":
            dizi[5] = "İlham"
            dizi = ilhamIkincil(dizi)

    elif dizi[0].lower() == "domination":
        dizi[0] = "Hakimiyet"
        dizi = hakimiyetBirincil(dizi)
        if dizi[5].lower() == "resolve":
            dizi[5] = "Azim"
            dizi = azimIkincil(dizi)
        elif dizi[5].lower() == "sorcery":
            dizi[5] = "Büyücülük"
            dizi = buyuculukIkincil(dizi)
        elif dizi[5].lower() == "precision":
            dizi[5] = "İsabet"
            dizi = isabetIkincil(dizi)
        elif dizi[5].lower() == "inspiration":
            dizi[5] = "İlham"
            dizi = ilhamIkincil(dizi)

    elif dizi[0].lower() == "sorcery":
        dizi[0] = "Büyücülük"
        dizi = buyuculukBirincil(dizi)
        if dizi[5].lower() == "resolve":
            dizi[5] = "Azim"
            dizi = azimIkincil(dizi)
        elif dizi[5].lower() == "precision":
            dizi[5] = "İsabet"
            dizi = isabetIkincil(dizi)
        elif dizi[5].lower() == "domination":
            dizi[5] = "Hakimiyet"
            dizi = hakimiyetIkincil(dizi)
        elif dizi[5].lower() == "inspiration":
            dizi[5] = "İlham"
            dizi = ilhamIkincil(dizi)

    elif dizi[0].lower() == "resolve":
        dizi[0] = "Azim"
        dizi = azimBirincil(dizi)
        if dizi[5].lower() == "precision":
            dizi[5] = "İsabet"
            dizi = isabetIkincil(dizi)
        elif dizi[5].lower() == "sorcery":
            dizi[5] = "Büyücülük"
            dizi = buyuculukIkincil(dizi)
        elif dizi[5].lower() == "domination":
            dizi[5] = "Hakimiyet"
            dizi = hakimiyetIkincil(dizi)
        elif dizi[5].lower() == "inspiration":
            dizi[5] = "İlham"
            dizi = ilhamIkincil(dizi)

    elif dizi[0].lower() == "inspiration":
        dizi[0] = "İlham"
        dizi = ilhamBirincil(dizi)
        if dizi[5].lower() == "resolve":
            dizi[5] = "Azim"
            dizi = azimIkincil(dizi)
        elif dizi[5].lower() == "sorcery":
            dizi[5] = "Büyücülük"
            dizi = buyuculukIkincil(dizi)
        elif dizi[5].lower() == "domination":
            dizi[5] = "Hakimiyet"
            dizi = hakimiyetIkincil(dizi)
        elif dizi[5].lower() == "precision":
            dizi[5] = "İsabet"
            dizi = isabetIkincil(dizi)

    dizi = nitelikSon(dizi)

    return dizi

def isabetBirincil(dizi):
    if dizi[1].lower() == "conqueror":
        dizi[1] = "Yenilmez"
    elif dizi[1].lower() == "fleet footwork":
        dizi[1] = "Ayağı Çabuk"
    elif dizi[1].lower() == "lethal tempo":
        dizi[1] = "Ölümcül Tempo"
    elif dizi[1].lower() == "press the attack":
        dizi[1] = "Saldırıya Devam"

    if dizi[2].lower() == "overheal":
        dizi[2] = "Şifa Taşkını"
    elif dizi[2].lower() == "triumph":
        dizi[2] = "Zafer"
    elif dizi[2].lower() == "presence of mind":
        dizi[2] = "Ölümcül Tempo"

    if "alacrity" in dizi[3].lower():
        dizi[3] = "Çeviklik"
    elif "tenacity" in dizi[3].lower():
        dizi[3] = "Sıvışma"
    elif "bloodline" in dizi[3].lower():
        dizi[3] = "Kan"

    if dizi[4].lower() == "coup de grace":
        dizi[4] = "Son Darbe"
    elif dizi[4].lower() == "cut down":
        dizi[4] = "Biç Devir"
    elif dizi[4].lower() == "last stand":
        dizi[4] = "Son Direniş"

    return dizi

def hakimiyetBirincil(dizi):
    if dizi[1].lower() == "electrocute":
        dizi[1] = "Elektrik Ver"
    elif dizi[1].lower() == "predator":
        dizi[1] = "Yırtıcı"
    elif dizi[1].lower() == "dark harvest":
        dizi[1] = "Kara Hasat"
    elif dizi[1].lower() == "hail of blades":
        dizi[1] = "Keskin Sağanak"

    if dizi[2].lower() == "cheap shot":
        dizi[2] = "Belden Aşağı"
    elif dizi[2].lower() == "taste of blood":
        dizi[2] = "Kan Tadı"
    elif dizi[2].lower() == "sudden impact":
        dizi[2] = "Ani Darbe"

    if dizi[3].lower() == "zombie ward":
        dizi[3] = "Zombi Totem"
    elif dizi[3].lower() == "ghost poro":
        dizi[3] = "Hayalet Poro"
    elif dizi[3].lower() == "eyeball collection":
        dizi[3] = "Gözyuvarı Koleksiyonu"

    if "ravenous" in dizi[4].lower():
        dizi[4] = "Açgözlü Avcı"
    elif "ingenious" in dizi[4].lower():
        dizi[4] = "Usta Avcı"
    elif "relentless" in dizi[4].lower():
        dizi[4] = "İnsafsız Avcı"
    elif "ultimate" in dizi[4].lower():
        dizi[4] = "Mükemmel Avcı"

    return dizi

def buyuculukBirincil(dizi):
    if dizi[1].lower() == "summon aery":
        dizi[1] = "Aery'i Çağır"
    elif dizi[1].lower() == "arcane comet":
        dizi[1] = "Sihirli Yıldız"
    elif dizi[1].lower() == "phase rush":
        dizi[1] = "Sürat Coşkusu"

    if dizi[2].lower() == "nullifying orb":
        dizi[2] = "Soğuran Küre"
    elif dizi[2].lower() == "manaflow band":
        dizi[2] = "Mana Akışı Yüzüğü"
    elif dizi[2].lower() == "nimbus cloak":
        dizi[2] = "Bulut Pelerini"

    if dizi[3].lower() == "transcendence":
        dizi[3] = "Yücelik"
    elif dizi[3].lower() == "celerity":
        dizi[3] = "Sürat"
    elif dizi[3].lower() == "absolute focus":
        dizi[3] = "Mutlak Odak"

    if dizi[4].lower() == "scorch":
        dizi[4] = "Kızart"
    elif dizi[4].lower() == "waterwalking":
        dizi[4] = "Suda Yürüyen"
    elif dizi[4].lower() == "gathering storm":
        dizi[4] = "Yaklaşan Fırtına"

    return dizi

def azimBirincil(dizi):
    if dizi[1].lower() == "grasp of the undying":
        dizi[1] = "Hortlağın Pençesi"
    elif dizi[1].lower() == "aftershock":
        dizi[1] = "Artçı Şok"
    elif dizi[1].lower() == "guardian":
        dizi[1] = "Muhafız"

    if dizi[2].lower() == "demolish":
        dizi[2] = "Tahrip"
    elif dizi[2].lower() == "font of life":
        dizi[2] = "Yaşam Kaynağı"
    elif dizi[2].lower() == "shield bash":
        dizi[2] = "Kalkan Darbesi"

    if dizi[3].lower() == "conditioning":
        dizi[3] = "Kondisyon"
    elif dizi[3].lower() == "second wind":
        dizi[3] = "İkinci Şans"
    elif dizi[3].lower() == "bone plating":
        dizi[3] = "Kemik Zırh"

    if dizi[4].lower() == "overgrowth":
        dizi[4] = "Aşırı Büyüme"
    elif dizi[4].lower() == "revitalize":
        dizi[4] = "Canlandır"
    elif dizi[4].lower() == "unflinching":
        dizi[4] = "Metanet"

    return dizi

def ilhamBirincil(dizi):
    if dizi[1].lower() == "glacial augment":
        dizi[1] = "Buzul Takviyesi"
    elif dizi[1].lower() == "unsealed spellbook":
        dizi[1] = "Dizginsiz Büyü Kitabı"
    elif dizi[1].lower() == "prototype: omnistone":
        dizi[1] = "Prototip Heptaş"

    if dizi[2].lower() == "hextech flashtraption":
        dizi[2] = "Hextech Sıçratıcısı"
    elif dizi[2].lower() == "magical footwear":
        dizi[2] = "Sihirli Pabuçlar"
    elif dizi[2].lower() == "perfect timing":
        dizi[2] = "Mükemmel Zamanlama"

    if dizi[3].lower() == "future's market":
        dizi[3] = "Geleceğin Pazarı"
    elif dizi[3].lower() == "minion dematerializer":
        dizi[3] = "Minyon Uçuran"
    elif dizi[3].lower() == "biscuit delivery":
        dizi[3] = "Peksimet Teslimatı"

    if dizi[4].lower() == "cosmic insight":
        dizi[4] = "Kozmik Sezgi"
    elif dizi[4].lower() == "approach velocity":
        dizi[4] = "Hızını Al"
    elif dizi[4].lower() == "time warp tonic":
        dizi[4] = "Zaman Büken Karışım"

    return dizi

def isabetIkincil(dizi):
    if dizi[6].lower() == "overheal":
        dizi[6] = "Şifa Taşkını"
    elif dizi[6].lower() == "triumph":
        dizi[6] = "Zafer"
    elif dizi[6].lower() == "presence of mind":
        dizi[6] = "Ölümcül Tempo"
    elif "alacrity" in dizi[6].lower():
        dizi[6] = "Çeviklik"
    elif "tenacity" in dizi[6].lower():
        dizi[6] = "Sıvışma"
    elif "bloodline" in dizi[6].lower():
        dizi[6] = "Kan"
    elif dizi[6].lower() == "coup de grace":
        dizi[6] = "Son Darbe"
    elif dizi[6].lower() == "cut down":
        dizi[6] = "Biç Devir"
    elif dizi[6].lower() == "last stand":
        dizi[6] = "Son Direniş"

    if dizi[7].lower() == "overheal":
        dizi[7] = "Şifa Taşkını"
    elif dizi[7].lower() == "triumph":
        dizi[7] = "Zafer"
    elif dizi[7].lower() == "presence of mind":
        dizi[7] = "Ölümcül Tempo"
    elif "alacrity" in dizi[7].lower():
        dizi[7] = "Çeviklik"
    elif "tenacity" in dizi[7].lower():
        dizi[7] = "Sıvışma"
    elif "bloodline" in dizi[7].lower():
        dizi[7] = "Kan"
    elif dizi[7].lower() == "coup de grace":
        dizi[7] = "Son Darbe"
    elif dizi[7].lower() == "cut down":
        dizi[7] = "Biç Devir"
    elif dizi[7].lower() == "last stand":
        dizi[7] = "Son Direniş"

    return dizi

def hakimiyetIkincil(dizi):
    if dizi[6].lower() == "cheap shot":
        dizi[6] = "Belden Aşağı"
    elif dizi[6].lower() == "taste of blood":
        dizi[6] = "Kan Tadı"
    elif dizi[6].lower() == "sudden impact":
        dizi[6] = "Ani Darbe"
    elif dizi[6].lower() == "zombie ward":
        dizi[6] = "Zombi Totem"
    elif dizi[6].lower() == "ghost poro":
        dizi[6] = "Hayalet Poro"
    elif dizi[6].lower() == "eyeball collection":
        dizi[6] = "Gözyuvarı Koleksiyonu"
    elif "ingenious" in dizi[6].lower():
        dizi[6] = "Usta Avcı"
    elif "relentless" in dizi[6].lower():
        dizi[6] = "İnsafsız Avcı"
    elif "ultimate" in dizi[6].lower():
        dizi[6] = "Mükemmel Avcı"

    if dizi[7].lower() == "cheap shot":
        dizi[7] = "Belden Aşağı"
    elif dizi[7].lower() == "taste of blood":
        dizi[7] = "Kan Tadı"
    elif dizi[7].lower() == "sudden impact":
        dizi[7] = "Ani Darbe"
    elif dizi[7].lower() == "zombie ward":
        dizi[7] = "Zombi Totem"
    elif dizi[7].lower() == "ghost poro":
        dizi[7] = "Hayalet Poro"
    elif dizi[7].lower() == "eyeball collection":
        dizi[7] = "Gözyuvarı Koleksiyonu"
    elif "ravenous" in dizi[7].lower():
        dizi[7] = "Açgözlü Avcı"
    elif "ingenious" in dizi[7].lower():
        dizi[7] = "Usta Avcı"
    elif "relentless" in dizi[7].lower():
        dizi[7] = "İnsafsız Avcı"
    elif "ultimate" in dizi[7].lower():
        dizi[7] = "Mükemmel Avcı"

    return dizi

def buyuculukIkincil(dizi):
    if dizi[6].lower() == "nullifying orb":
        dizi[6] = "Soğuran Küre"
    elif dizi[6].lower() == "manaflow band":
        dizi[6] = "Mana Akışı Yüzüğü"
    elif dizi[6].lower() == "nimbus cloak":
        dizi[6] = "Bulut Pelerini"
    elif dizi[6].lower() == "transcendence":
        dizi[6] = "Yücelik"
    elif dizi[6].lower() == "celerity":
        dizi[6] = "Sürat"
    elif dizi[6].lower() == "absolute focus":
        dizi[6] = "Mutlak Odak"
    elif dizi[6].lower() == "scorch":
        dizi[6] = "Kızart"
    elif dizi[6].lower() == "waterwalking":
        dizi[6] = "Suda Yürüyen"
    elif dizi[6].lower() == "gathering storm":
        dizi[6] = "Yaklaşan Fırtına"

    if dizi[7].lower() == "nullifying orb":
        dizi[7] = "Soğuran Küre"
    elif dizi[7].lower() == "manaflow band":
        dizi[7] = "Mana Akışı Yüzüğü"
    elif dizi[7].lower() == "nimbus cloak":
        dizi[7] = "Bulut Pelerini"
    elif dizi[7].lower() == "transcendence":
        dizi[7] = "Yücelik"
    elif dizi[7].lower() == "celerity":
        dizi[7] = "Sürat"
    elif dizi[7].lower() == "absolute focus":
        dizi[7] = "Mutlak Odak"
    elif dizi[7].lower() == "scorch":
        dizi[7] = "Kızart"
    elif dizi[7].lower() == "waterwalking":
        dizi[7] = "Suda Yürüyen"
    elif dizi[7].lower() == "gathering storm":
        dizi[7] = "Yaklaşan Fırtına"

    return dizi

def azimIkincil(dizi):
    if dizi[6].lower() == "demolish":
        dizi[6] = "Tahrip"
    elif dizi[6].lower == "font of life":
        dizi[6] = "Yaşam Kaynağı"
    elif dizi[6].lower == "shield bash":
        dizi[6] = "Kalkan Darbesi"
    elif dizi[6].lower() == "conditioning":
        dizi[6] = "Kondisyon"
    elif dizi[6].lower == "second wind":
        dizi[6] = "İkinci Şans"
    elif dizi[6].lower == "bone plating":
        dizi[6] = "Kemik Zırh"
    elif dizi[6].lower() == "overgrowth":
        dizi[6] = "Aşırı Büyüme"
    elif dizi[6].lower == "revitalize":
        dizi[6] = "Canlandır"
    elif dizi[6].lower == "unflinching":
        dizi[6] = "Metanet"

    if dizi[7].lower() == "demolish":
        dizi[7] = "Tahrip"
    elif dizi[7].lower == "font of life":
        dizi[7] = "Yaşam Kaynağı"
    elif dizi[7].lower == "shield bash":
        dizi[7] = "Kalkan Darbesi"
    elif dizi[7].lower() == "conditioning":
        dizi[7] = "Kondisyon"
    elif dizi[7].lower == "second wind":
        dizi[7] = "İkinci Şans"
    elif dizi[7].lower == "bone plating":
        dizi[7] = "Kemik Zırh"
    elif dizi[7].lower() == "overgrowth":
        dizi[7] = "Aşırı Büyüme"
    elif dizi[7].lower == "revitalize":
        dizi[7] = "Canlandır"
    elif dizi[7].lower == "unflinching":
        dizi[7] = "Metanet"

    return dizi

def ilhamIkincil(dizi):
    if dizi[6].lower() == "hextech flashtraption":
        dizi[6] = "Hextech Sıçratıcısı"
    elif dizi[6].lower() == "magical footwear":
        dizi[6] = "Sihirli Pabuçlar"
    elif dizi[6].lower() == "perfect timing":
        dizi[6] = "Mükemmel Zamanlama"
    elif dizi[6].lower() == "future's market":
        dizi[6] = "Geleceğin Pazarı"
    elif dizi[6].lower() == "minion dematerializer":
        dizi[6] = "Minyon Uçuran"
    elif dizi[6].lower() == "biscuit delivery":
        dizi[6] = "Peksimet Teslimatı"
    elif dizi[6].lower() == "cosmic insight":
        dizi[6] = "Kozmik Sezgi"
    elif dizi[6].lower() == "approach velocity":
        dizi[6] = "Hızını Al"
    elif dizi[6].lower() == "time warp tonic":
        dizi[6] = "Zaman Büken Karışım"

    if dizi[7].lower() == "hextech flashtraption":
        dizi[7] = "Hextech Sıçratıcısı"
    elif dizi[7].lower() == "magical footwear":
        dizi[7] = "Sihirli Pabuçlar"
    elif dizi[7].lower() == "perfect timing":
        dizi[7] = "Mükemmel Zamanlama"
    elif dizi[7].lower() == "future's market":
        dizi[7] = "Geleceğin Pazarı"
    elif dizi[7].lower() == "minion dematerializer":
        dizi[7] = "Minyon Uçuran"
    elif dizi[7].lower() == "biscuit delivery":
        dizi[7] = "Peksimet Teslimatı"
    elif dizi[7].lower() == "cosmic insight":
        dizi[7] = "Kozmik Sezgi"
    elif dizi[7].lower() == "approach velocity":
        dizi[7] = "Hızını Al"
    elif dizi[7].lower() == "time warp tonic":
        dizi[7] = "Zaman Büken Karışım"

    return dizi

def nitelikSon(dizi):
    if dizi[8].lower() == "attack speed":
        dizi[8] = "Saldırı Hızı"
    elif dizi[8].lower() == "adaptive force":
        dizi[8] = "Değişken Kuvvet"
    elif dizi[8].lower() == "scaling cooldown reduction":
        dizi[8] = "Bekleme Süresinde Azalma"

    if dizi[9].lower() == "armor":
        dizi[9] = "Zırh"
    elif dizi[9].lower() == "adaptive force":
        dizi[9] = "Değişken Kuvvet"
    elif dizi[9].lower() == "magic resist":
        dizi[9] = "Büyü Direnci"

    if dizi[10].lower() == "scaling health":
        dizi[10] = "Can"
    elif dizi[10].lower() == "magic resist":
        dizi[10] = "Büyü Direnci"
    elif dizi[10].lower() == "armor":
        dizi[10] = "Zırh"

    return dizi
