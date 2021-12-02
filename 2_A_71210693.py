nama = []
no_kursi = []
repeat = 0

while(repeat < 1):
    n = input("Masukkan nama : ")
    if n == "STOP":
        break
    else:
        k = int(input("Masukkan nomor kursi "+n+": "))

    if k in no_kursi:
        print("Mohon maaf kursi tersebut telah terisi!")
    else:
        nama.append(n)
        no_kursi.append(k)

print("\nList kursi yang telah terisi : ")

for a in range (0,len(no_kursi),1):
    print("Kursi nomor", no_kursi[a], "telah diisi oleh", nama[a])