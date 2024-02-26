inputbulan = input("masukkan bulan yang(1-12) : ")

try:
    bulan = int(inputbulan)
    if bulan == 1:
        print("bulan ini berjumlah 31 hari")
    elif bulan == 2:
        print("bulan ini berjumlah 29 hari")
    elif bulan == 3:
        print("bulan ini berjumlah 31 hari")
    elif bulan == 4:
        print("bulan ini berjumlah 30 hari")
    elif bulan == 5:
        print("bulan ini berjumlah 31 hari")
    elif bulan == 6:
        print("bulan ini berjumlah 30 hari")
    elif bulan == 7:
        print("bulan ini berjumlah31 hari")
    elif bulan == 8:
        print("bulan ini berjumlah 31 hari")
    elif bulan == 9:
        print("bulan ini berjumlah 30 hari")
    elif bulan == 10:
        print("bulan ini berjumlah 31 hari")
    elif bulan == 11:
        print("bulan ini berjumlah 30 hari")
    elif bulan == 12:
        print("bulan ini berjumlah 31 hari")
    else :
        print("bulan yang diinputkan oleh pengguna tersebut tidak valid")
except  :
    print("masukkan kembali dalam bilangan bulat")
        
    