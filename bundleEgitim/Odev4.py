# SORU 1

def find_age(name,age):
    print(f"{name} is {age} years old.")


# SORU 2

def reverse_string(str):
    print(str[::-1])


# SORU 3



def change_number(numbers):
    
    index = 0

    for number in len(change_number(numbers)):

        if numbers[number]%2 == 0:
            numbers[number] +=1
        else:
            numbers[number] -=1
            
        index += 1
    
    return numbers



x = input("Sayıyı giriniz: ")
print(change_number(x))



# SORU 4

def faktöryel(sayi):
    deger = 1

    for i in range(1 , sayi+1):
        deger*= i
    
    return deger


def combination(number1,number2):
    kombinasyon = faktöryel(number1)/(faktöryel(number2)*faktöryel((number1-number2)))

    return kombinasyon


print(combination(5,2))

