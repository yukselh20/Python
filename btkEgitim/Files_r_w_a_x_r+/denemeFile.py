def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3

    if ortalama > 90 and ortalama < 100:
        harf = "AA"
    elif ortalama >75 and ortalama < 90:
        harf = "BB"
    elif ortalama > 50 and ortalama < 75:
        harf = "CC"
    else:
        harf = "FF"

    return ogrenciAdi+ ":" +harf + "\n"
    


def not_oku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
            
            
            

def not_gir():
    ad = input("Öğrencinin ismini giriniz: ")
    soyad = input("Öğrencinin soyadını giriniz: ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")

    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(ad+ " "+ soyad+":"+not1+","+not2+","+not3 + "\n") 


def not_kaydet():
    with open("notlar.txt","r",encoding="utf-8") as file:
        liste = []

        for notlar in file:
            liste.append(not_hesapla(notlar))

        with open("sonuçlar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:
    islem = input("\n1) Notları oku\n2) Not gir\n3) Notları kaydet\n4) Çıkış\n")

    if islem == "1":
        not_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kaydet()
    elif islem == "4":
        break