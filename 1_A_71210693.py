deret = input("Masukkan deret angka : ")
pembatas = deret.split(",")
hitung = len(pembatas)

if(int(pembatas[0]) % 2 == 0):
    mulai = pembatas[0]
    sum = int(mulai)
else:
    mulai = int(pembatas[0])*-1
    sum = int(mulai)

print("Total :",mulai,end="")

for agk in pembatas[1:hitung]:
    if(agk != pembatas[0]):
        if(int(agk) % 2 == 1):
            agk = int(agk) * -1
            sum = sum + int(agk)
            print("",agk,end="")
        elif(int(agk) % 2 == 0):
            sum = sum + int(agk)
            if(agk == pembatas[0]):
                print(agk,end="")
            else:
                print(" +",agk,end="")

print()
print("Hasil perhitungan diatas ialah",sum)