n=int(input("Give your range :"))
for i in range(n):
    for k in range(i,n):
        print(" ",end= " ")
    for j in range(i+1):
        print("*",end= " ")
    for j in range(i):
        print("*",end= " ")

    print()