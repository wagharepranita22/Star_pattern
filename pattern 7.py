n=int(input("Give your range :"))
for i in range(n):
    for j in range(i):
        print(" ",end= "  ")
    for k in range(i,n):
        print("*",end= "  ")
    print()