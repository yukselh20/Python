sampleString = """ Phyton's name does not come from a  
'snake'""" # 3 tırnak işareti ile yazılan stringler aynı şekilde bastırılır.

print(sampleString)


name = "Atilla"
surname = "İlhan"

formattedMassage = f"{name} [{surname}] is poet"

formattedMassage1 = f"{name:10} [{surname:10}] is poet"

formattedMassage2 = f"{name:.2} [{surname:.2}] is poet"

print(formattedMassage)
print(formattedMassage1)
print(formattedMassage2)


print("******************************************************************************")

example = "this is an example"

print(f"{example:*>50}")
print(f"{example:*<50}")
print(f"{example:*^50}")
print(f"{example:*^50}")

print("******************************************************************************")

userString = input("Enter your string: ")
userString = userString[-3: ] + userString[0:3]
# sondan 3 karakter alır.

print(userString.upper())

