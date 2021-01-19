def func():
    return 10 + 5

def func2():
    print(10+5)

# Birinci fonksiyonda döner 2. Fonksiyonda yazdırır.

result1 = func()
result2 = func2()

print(f"Result 1, {result1}") #return ile döndüğü için atanabilir
print(f"Result 2, {result2}") #tek seferlik print eder değere atanmaz.

# set fonksiyonu sıralar ve çoklu elemanları teke indirir.

my_list = [1,5,7,8,10,2,3,5,8]

h = set(my_list)
print(h)

y = lambda a : a**2

print(y(8))

print("****************************************************************************")

def yasHesapla(dogumyili):
    return 2020-dogumyili


def emeklilikYasinaKalanHesapla(dogumyili, isim):
    yas = yasHesapla(dogumyili)
    emeklilik = 65-yas

    if emeklilik > 0:
        print(f"Sayın {isim} emekliliğinize {emeklilik} yıl kaldı")

    else:
        print(f"Zaten {-1*emeklilik} yıldır emeklisiniz.")

emeklilikYasinaKalanHesapla(1984,"Ahmet")
emeklilikYasinaKalanHesapla(1950,"Hamza")

print("****************************************************************************")


def displayuser(**args): # çifr yıldız dictionary oluşturur.
    for key , value in args.items():
        print("{} is {}".format(key,value))

displayuser(name = "Hamza", age = 19 , surname = "Yüksel", email = "hamza123@gmail.com") 

print("****************************************************************************")

def myFunc(a,b,*args,**params):
    print(a)
    print(b)
    print(args)
    print(params)

myFunc(10,20,40,"hamza","furkan",name="gıda",yas=19) #arglar tuple, paramlar dict sözlük oluşturdu

print("****************************************************************************")

def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi >1:
            for i in range(2,sayi):
                if sayi%i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input("1. sayiyi giriniz: "))
sayi2 = int(input("2. sayiyi giriniz: "))

asalSayilariBul(sayi1,sayi2)

print("****************************************************************************")

def tamBolenBulma(xx):
    tambolenler = []

    for i in range(2,xx):
        if xx % i ==0:
            tambolenler.append(i)
    return tambolenler
        

result = tamBolenBulma(20)
print(result)

print("****************************************************************************")


        