from random import choice



class Mp3Calar():
    def __init__(self,sarkilarListesi=[]):
        self.sarkilarListesi = sarkilarListesi
        self.suanCalanSarkı = ""
        self.ses = 100
        self.durum = True
        

    
    def menuSecim(self):
        print("""
Şarkı listesi = {}
Şuan çalan şarkı = {}
Ses yüksekliği = {}

1) Sarkı seç
2) Ses azalt
3) Ses yükselt
4) Rastgele şarkı seç
5) şarkı ekle
6) Şarkı sil
7) Kapat
""".format(self.sarkilarListesi,self.suanCalanSarkı,self.ses))
    
    def secim(self):
        sec = int(input("Seçiminizi yapınız: "))

        while sec < 1 or sec > 7:
            sec = int(input("Seçiminizi tekrar yapınız (1 ile 7 arasında): "))

        return sec
    
    def calistir(self):
        self.menuSecim()
        secim = self.secim()

        if secim == 1:
            self.sarkiSec()
        if secim == 2:
            self.sesAzalt()
        if secim == 3:
            self.sesArttir()
        if secim == 4:
            self.rastgeleSarkiSec()
        if secim == 5:
            self.sarkiEkle()
        if secim == 6:
            self.sarkiSil()
        if secim == 7:
            self.kapa()
        
         
    def sarkiSec(self):
        sayac = 1
        for sarki in self.sarkilarListesi:
            print("{}){}".format(sayac,sarki))
            sayac +=1
        
        sarkiSec = int(input("Silmek istediğiniz şarkının numarasını giriniz: "))

        while sarkiSec < 1 or sarkiSec > len(self.sarkilarListesi):
            sarkiSec = int(input("Lütfen liste uzunluğu arasında seçim yapınız: "))
        
        self.suanCalanSarkı = self.sarkilarListesi[sarkiSec - 1]

    def sesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10

    def sesArttir(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10 
    
    def rastgeleSarkiSec(self):
        random_sarki = choice(self.sarkilarListesi)
        self.suanCalanSarkı = random_sarki

    def sarkiEkle(self):
        sarkici = input("Eklemek istediğiniz sanatçının/grubun adını giriniz: ")
        sarki = input("Eklemek istediğiniz şarkının adını girinizi: ")
        self.sarkilarListesi.append(sarkici + "-" + sarki)

    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarkilarListesi:
            print("{}){}".format(sayac,sarki))
            sayac +=1
        
        numara = int(input("Silmek istediğiniz şarkının numarasını giriniz: "))

        while numara < 1 or numara > len(self.sarkilarListesi):
            numara = int(input("Lütfen liste uzunluğu arasında seçim yapınız: "))
        
        self.sarkilarListesi.pop(numara - 1)

    def kapa(self):
        self.durum = False
        print("Program sonlandı.")



mp3calar = Mp3Calar()

while mp3calar.durum:
    mp3calar.calistir()

