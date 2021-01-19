#SORU1 verilen listenin sıralanmış olup olmadığını kontrol etme.
numbers = []

while True:
    number = input("Liste oluşturmak için sayıları teker teker girip enterlayın. çıkmak için ise SADECE ENTER A basın yapın: ")
    if number == "":
        break
    numbers.append(int(number))

sortedlist = sorted(numbers)


if sortedlist == numbers:
    print(f"Original list: {numbers}.\nTRUE.")

else:
    print(f"Original list: {numbers}.\nFALSE. Sorted version of list is: {sortedlist}")



#SORU 2 1. liste ile 2. listede bulunan elemanları çıkarma

liste1 = list(input("1. liste için sayıları giriniz: "))
liste2 = list(input("2. liste için sayıları giriniz: "))

sonliste=[]


for sayilar in liste1:
    if sayilar in liste2:
        continue
    else:
        sonliste.append(sayilar)

print("Birinci liste: ", liste1)
print("İkinci liste: ", liste2)
print("Son liste: ", sonliste)


#SORU 3

listem = ["elma","armut","portakal","muz"]

listem.append("kiraz")  #kiraz stringini listeye ekler
listem.count("elma")  #elma ögesinin sayısını gösterir
listem.index("muz")    #muzun listedeki sırasını gösterir
listem.sort()  #liste stringse alfabetik, numerikse sayısal olarak listeyi sıralar.
listem.reverse()  # listenin sırasını yer değiştirir.
listem.insert() # belirtilen index numarasıba eleman ekler.



isim = {'isim': 'Mehmet','soyisim':'Yılmaz', 'yas': 24}

print(isim)          # isim adlı sözlüğün tüm değerlerini ekrana basar
print(isim.keys())   #isim adlı sözlüğün tüm key'lerini ekrana basar
print(isim.values()) # isim adlı sözlüğün tüm value'lerini ekrana basar
print(isim.items()) #Hem keyleri hem de value leri yazdırır
isim2= isim.copy() #isim sözlüğünü isim2 olarak kopyalar
#isim.clear() sözlüğün içeriğini siler.
isim.pop("soyisim") #Soyisim değerini siler

liste_1 ={"Ali":70,"Mehmet":50,"Kemal":60,"Mustafa":75}
liste_2 ={"Ali":80,"Mehmet":60,"Kemal":70,"Mustafa":85}

liste_1.update(liste_2)  # liste_1 i liste_2 olarak günceller.



#SORU 4 Harf sayısı hesaplama :(

soru = input("Bir kelime giriniz: ").replace(" ","")

ortak = list(soru)
say = {}

for z in ortak:
    say[z] = ortak.count(z)

print(say)

    




# SORU 5
c1 = input("1. değeri giriniz.")
c2 = input("2. değeri giriniz.")
c3 = input("3. değeri giriniz.")
c4 = input("4. değeri giriniz.")
c5 = input("5. değeri giriniz.")

while True:
    for a in range(5):
        print(c1,end=" ")
          
    for b in range(4):
        print(c2,end=" ")

    for c in range(3):
        print(c3,end=" ")

    for d in range(2):
        print(c4,end=" ")

    for e in range(1):
        print(c5,end=" ")
    break

# satir = 5
# for i in range(satir):
#     print(f'{c1} '*(satir-))