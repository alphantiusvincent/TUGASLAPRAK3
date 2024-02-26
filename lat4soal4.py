# Sebuah program meminta pengguna memasukkan ketiga panjang sisi suatu segitiga
# (berarti pengguna memasukkan tiga bilangan). Jika ketiga sisi segitiga tersebut semuanya sama,
# tampilkan pesan: "3 sisi sama". Jika hanya ada dua sisi yang sama panjang, tampilkan pesan "2
# sisi sama". Jika tidak ada yang sama maka tampilkan pesan: "Tidak ada yang sama". Sebagai
# contoh, perhatikan input dan output berikut ini:
try:
    panjang1 = int(input("masukkan panjang 1: "))
    panjang2 = int(input("masukkan panjang 2: "))
    panjang3 = int(input("masukkan panjang 3: "))


    if panjang1 == panjang2 == panjang3:
        print("3 sisi sama")
    elif panjang1 == panjang2 or panjang1 == panjang3 or panjang2 ==panjang3:
        print("2 sisi sama")
    else:
        print("tidak ada sisi yang sama")
except:
    print("masukkin angka")
    