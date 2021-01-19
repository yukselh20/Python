class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma= True
    
    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanEkle()      
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            ay_yil_maas = input("Verilecek maaşları yıllık bazda görmek ister misiniz (e/h)?")
            if ay_yil_maas == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()
        if secim == 4:
            self.maaslarıVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input(f"***{self.ad} Otomasyonuna Hoşgeldiniz.***\n\n1)Çalışan ekleme\n2)Çalışan çıkarma\n3)Verilecek maaş göster\n4)Maaşları verme\n5)Masraf gir\n6)Gelir gir\n\nSeçiminizi giriniz:"))
        if secim<1 or secim>6:
            secim = int(input("Lütfen 1-6 arasında bir seçim yapınız!"))
        return secim

    def calisanEkle(self):
        id = 1
        ad = input("Çalışanın adını giriniz: ")
        soyad = input("Çalışanın soyadını giriniz: ")
        cinsiyet = input("Çalışanın cinsiyetini giriniz: ")
        yas = input("Çalışanın yaşını giriniz: ")
        maas = input("Çalışanın maasını giriniz: ")

        with open("calisanlar.txt","r") as dosya:
            calisanlarListesi = dosya.readlines()

        if len(calisanlarListesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt","r") as dosya:
                id = int(calisanlarListesi[-1].split(")")[0])  +1

        
        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,cinsiyet,yas,maas))


    def calisanCikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        gosterCalisanlar = []

        for calisan in calisanlar:
            gosterCalisanlar.append(" ".join(calisan[:-1].split("-"))) #Calısan(1 numara mesela) baştan -1 e kadar
            #girmemizin nedeni son karakter \n dir. ve onun alınmaması lazım.

        for calisan in gosterCalisanlar:
            print(calisan)

        secim = int(input(f"Lütfen çıkarmak istediğiniz çalışanın numarasını giriniz (1-{len(gCalisanlar)}): "))
        while secim < 1 or secim > len(gCalisanlar):
            int(input(f"Lütfen değer aralığında bir sayı seçiniz! (1-{len(gCalisanlar)}):"))

        calisanlar.pop(secim-1) ## Calisanlar listesinden seçicehi rakam seçimin -1 indexi olur.
        ## çalısanlardan birini silince id no lar karışır

        degisenCalisan = []

        
        numara = 1
        for calisan in calisanlar:
            degisenCalisan.append(str(numara) + ")" + calisan.split(")")[1])# calısan sildiğimizde id nosu kayar
            # bu yüzden id den sonra gelen kısma yeni değişken ekliyoruz. numara değişkeni.
            numara += 1


        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(degisenCalisan)

    def verilecekMaasGoster(self, hesap = 'a'):
        """hesap: yıllık için y , aylık için a harfi kullanılacak."""
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        if hesap == "a":
            print(f"Bu ay ödenmesi gereken toplam maaşlar: {sum(maaslar)}")
        else:
            print(f"Bu yıl ödenmesi gereken toplam maaşlar: {sum(maaslar)*12}")


    def maaslarıVer(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

            toplamMaas = sum(maaslar)

        ### Bütceden Maası alma ###

        with open("butce.txt","r") as dosya:
            tButce = int(dosya.readlines()[0])

        tButce = tButce - toplamMaas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tButce))

        print(f"Bütçenin son durumu : {tButce}")



    def masrafGir(self):
        pass

    def gelirGir(self):
        pass




sirket = Sirket("Hamza Elektronik.")

while sirket.calisma:    
    sirket.program()