masukan = str(input("Input : "))
print("Output : ",end="")
p = len(masukan)

for k in range(0,p,1):
    for b in range(0,k,1):
        print(masukan[b], end='')
    print('')
for k in range(p,0,-1):
    for b in range(0, k):
        print(masukan[b],end='')
    print('')