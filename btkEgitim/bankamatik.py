Hamzahesap={
    "hesapNo" : 123456,
    "ad" : "Hamza",
    "bakiye" : 2000,
    "ekHesapBakiye" : 3000
}

def paraCek(hesap,miktar):
    if hesap["bakiye"] >= miktar:
        print("Paranızı çekebilirsiniz.")
        hesap["bakiye"] = hesap["bakiye"] - miktar
    
    else:
        toplam = hesap["bakiye"] + hesap["ekHesapBakiye"]
        ekHesapKullanimi = input("Ek hesap bakiyesini kullanmak istiyor musunuz? (e/h)")

        if ekHesapKullanimi == "e":
            if toplam > miktar:
                print("ek hesap ile para çekimi başarılı")
                hesap["bakiye"] = 0
                hesap["ekHesapBakiye"] = toplam - miktar
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bakiye bulunmaktadır.")
        else:
            print("Toplam bakiye yetersiz")  


paraCek(Hamzahesap , 2000)
paraCek(Hamzahesap, 2000)
print(Hamzahesap) 
