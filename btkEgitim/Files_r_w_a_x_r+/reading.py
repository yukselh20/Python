# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nHamza Yüksel")

iki = open("newfile.txt","r",encoding="utf-8")

# for i in iki:
#     print(i, end="")

# content = iki.readline() ## line line okur. sıra ile teker teker okur.
# content = iki.readlines() ## dosyadaki bilgileri listeler.
# print(content)
# file.close()
iki.close()

with open("newfile2.txt","r",encoding="utf-8") as file2:
    content = file2.read()
    print(content)
    print(file2.tell()) #Kürsünün dosyadaki konumunu verir.
    file2.seek(25) #Kürsünün konumunu ayarlamaya yarar.
    content2 =file2.read()
    print(content2)
    print(file2.tell())
    
