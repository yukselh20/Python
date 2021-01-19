class Personel():
    def __init__(self,ad,soyad,cinsiyet,yas,maas):
        self.ad = ad
        self.soyad = soyad
        self.cinsiyet = cinsiyet
        self.yas = yas
        self.maas = maas

    def bilgileriYazdir(self):
        print("""
{} {} Bilgileri Şunlardır:
Yaş: {}
Cinsiyet: {}
Maaş: {}

        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))

    def __str__(self):
        return """
{} {} Bilgileri Şunlardır:
Yaş: {}
Cinsiyet: {}
Maaş: {}

        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas)



class Yonetici(Personel):
    def __init__(self,ad,soyad,cinsiyet,yas,maas):
        super().__init__(ad,soyad,cinsiyet,yas,maas)

    def maasArttır(self,pObject,arttirmaMiktari=1000):
        pObject.maas += arttirmaMiktari




personel = Personel("Hamza","Yüksel","Erkek",19,5000)

yonetici = Yonetici("Mehmet","Yüksel","Erkek","65",12000)

yonetici.maasArttır(personel,212541)

print(personel)
