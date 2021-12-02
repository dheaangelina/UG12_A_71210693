nilai_n = int(input("Input : "))
s = 2

for i in range(1,nilai_n+1):
    for j in range(1,2*nilai_n):
        if i+j == nilai_n+1 or j-i == nilai_n-1:
            print('*', end="")
        elif i == nilai_n and j!=s:
            print('*', end="")
            s = s + 2
        else:
            print(end=" ")
    print()