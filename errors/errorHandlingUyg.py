liste = ["1","20","1a0","24i","10","50"]

## Liste elemanlarının sayısal olanlarını yazdırın.

sayisal = []

for sayi in liste:
    try:
        int(sayi)/int(sayi)
    except Exception as ex:
        print(ex)
    else:
        sayisal.append(sayi)

print(sayisal)

print("**********************************************************************")

x =input("Sayısal bir değer giriniz.")

while True:
    x = input("Sayısal bir değer giriniz.")
    if x == "q":
        break

    try:
        result = int(x)
        print(result)
    except Exception as dd:
        print(dd)
        continue

