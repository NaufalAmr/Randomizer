import random as r

def rollADice():
    result = 0
    dice = int(input("Jumlah dadu : "))
    while True:
        for _ in range(0,dice):
            result+=r.randint(1, 6)
        print(result)
        userReq = input("Lempar dadu lagi? [y/n] : ")
        if userReq == "n":
            break
        else:
            result = 0
    

def flipCoin():
    while True:
        print(r.choice(["kepala", "ekor"]), "!!")
        userReq = input("Lempar koin lagi? [y/n] : ")
        if userReq == "n":
            break

def randomNumber():
    numRange = input("masukkan range angka (misal 1-10) : ")
    data = numRange.split("-")
    while True:
        print(r.randint(int(data[0]), int(data[1])))
        userCmnd = input("Acak lagi ? [y/n] : ")
        if userCmnd == "n":
            break

def randomName():
    count = int(input("Jumlah nama yg akan diacak : "))
    nameData = []
    for _ in range(0,count):
        name = input("Masukkan nama : ")
        nameData.append(name)
    print("""
1.Ambil satu nama
2.Buat urutan nama acak
========================""")
    userReq = input("Masukkan pilihan : ")
    
    while True:
        if userReq == "1":
            print(r.choice(nameData))
        elif userReq == "2":
            r.shuffle(nameData)
            for key,val in enumerate(nameData, start=1):
                print(f"{key}.{val}")
        userCmnd = input("Acak lagi ? [y/n] : ")
        if userCmnd == "n":
            break

def main():
    while True:
        print("""
==================
    RANDOMIZER
==================
1. Lempar dadu
2. Lempar koin
3. Acak angka
4. Acak nama""")
        userRequest = input("Masukkan nomor pillihan : ")
        if userRequest == "1":
            rollADice()
        elif userRequest == "2":
            flipCoin()
        elif userRequest == "3":
            randomNumber()
        elif userRequest == "4":
            randomName()

if __name__ == "__main__":
    main()