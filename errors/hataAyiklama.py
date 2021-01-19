while True:
    try:
        boy = float(input("Boyunuzu metre cinsinden giriniz (1.70): "))
        break
    except ValueError:
        print("Doğru değer giriniz.")

while True:
    try:
        kilogram = float(input("Kilonuzu kg cinsinden giriniz (85.7): "))
        break
    except ValueError:
        print("Doğru bir değer giriniz!!!")

index = kilogram/boy**2

print(f"boy kilo endexiniz: {index}")