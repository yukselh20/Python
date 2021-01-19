def tcNoDogruMu(kimlikNo:str):
    evenNumbers = 0
    oddNumbers = 0
    numbersSum = 0
    index = 1

    if len(kimlikNo) != 11:
        return False1
    return True

    if kimlikNo[0] != '0':
        return False
    return True


    for number in kimlikNo:
        numbersSum += int(number)
        
        if index>9:
            break
        
        if index % 2 == 0 :
            evenNumbers += int(number)
        else:
            oddNumbers += int(number)

        index += 1
    
    onuncuHane = (oddNumbers*7 - evenNumbers)%10

    if onuncuHane == int(tcNoDogruMu[9]) and numbersSum % 10 == int(tcNoDogruMu[10]):
        return True
    return False


tcno = input("Tc numaranızı giriniz: ")

if tcNoDogruMu(tcno):
    print("Idendity verified.")
else:
    print("Idendity is not verified.")