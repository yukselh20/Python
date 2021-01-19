import random

print("***************************************************************************")

# SORU 1
ogr_notu = int(input("Öğrencinin Notunu Giriniz: "))

if ogr_notu>=90 and ogr_notu<=100:
    print("Öğrencinin harf notu: AA")

elif ogr_notu>=80 and ogr_notu<90:
    print("Öğrencinin harf notu: BA")

elif ogr_notu>=70 and ogr_notu<80:
    print("Öğrencinin harf notu: BB")

elif ogr_notu>=60 and ogr_notu<70:
    print("Öğrencinin harf notu: CB")

elif ogr_notu>=50 and ogr_notu<60:
    print("Öğrencinin harf notu: DD")

elif ogr_notu>=40 and ogr_notu<50:
    print("Öğrencinin harf notu: DC")

elif ogr_notu>=30 and ogr_notu>40:
    print("Öğrencinin harf notu: DD")

elif ogr_notu>=20 and ogr_notu<30:
    print("Öğrencinin harf notu: FF")

else:
    print("Öğrencinin harf notu: VF")

print("***************************************************************************")

# SORU 2
i=0 
toplam = 0

while i<=100000:
    toplam = i + toplam
    i+=1

print(f"100000' e kadar olan sayıların toplamı: {toplam}")

print("***************************************************************************")

# SORU 3
oyun=True

sayi = random.randint(0,10000)

while oyun:

    tahmin = input("Enter the number: ")

    if tahmin.isdigit():
        tahmin = int(tahmin)

        if tahmin == sayi:
            print("Congratulations, you won!!")
            oyun = False
        
        elif tahmin < sayi:
            print("Your number is too low.")
        
        else:
            print("Your number is too high.")

    else:
        if tahmin == 'end':
            oyun= False

        else:
            print("If you want to exit, you can press -end-")
