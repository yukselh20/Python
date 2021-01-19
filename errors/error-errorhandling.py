# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print("Lütfen sayısal bir değer giriniz.")
#     print(e)

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except Exception as ex:
    print("Lütfen sayısal bir değer giriniz.", ex)




##### Raising the exception (sorunu kendi kuralına göre belirleme)


def checkPassword(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakter içermelidir.")
    elif  not re.search("[a-z]",psw):
        raise Exception("Parolanız en az 1 adet küçük harf içermelidir.")
    elif  not re.search("[A-Z]",psw):
        raise Exception("Parolanız en az 1 adet büyük harf içermelidir.")
    elif  not re.search("[0-9]",psw):
        raise Exception("Parolanız en az 1 adet rakam içermelidir.")
    elif  not re.search("[@#_-$]",psw):
        raise Exception("Parolanız en az 1 adet alpha numeric işaretler içermelidir.")
    elif  not re.search("[a-z]",psw):
        raise Exception("Parolanız en az 1 adet küçük harf içermelidir.")
    elif re.search("[\s]",psw):
        raise Exception("Parolanız boşluk karakteri içermemelidir.")


parola = "1234567"

try:
    checkPassword(parola)
except Exception as ex:
    print(ex)
else:
    print("Parola geçerlidir.")
finally:
    print("validation tamamlandı.")

    
