# # def outer(num):
#     print("outer")
#     def inner_func(num2):
#         print("inner")
#         return num + 5
#     num2 = inner_func(num)
#     print(num2)

# # outer(55)

# # def factorial(number):
#     if not isinstance(number,int):
#         raise TypeError("Value must be an intager number")
#     elif not number >=0:
#         raise ValueError("Value must be zero or positive.")

#     def inner_factorial(number):
#         if number == 1:
#             return 1 
        
#         return number * inner_factorial(number-1)

#     return inner_factorial(number)


# faktoryel = factorial(-5)
# print(faktoryel)


def islem(islem_adi):
    
    def toplam(*args):
        toplam = 0

        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpim = 1

        for i in args:
            carpim *=i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma



toplam = islem("toplama")
print(toplam(1,2,3,56,474,4))