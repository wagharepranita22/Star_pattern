n=int(input("Give the range  : "))
for i in range(n+1):
    for j in range(i):
        print(" ",end= " ")
    for j in range(i,n):
        print("*",end= " ")
    print()