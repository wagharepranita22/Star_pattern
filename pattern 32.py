n=int(input("Give your  n value : "))
for i in range(n):
    for k in range(i+1):
        if k == i or k == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")

    for k in range(i + 1):
        if  k == i or k == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n):
    for k in range(i,n):
        if k == n - 1 or k == i :
            print("*", end=" ")
        else:
            print(" ", end=" ")

    for j in range(i):
        print(" ", end=" ")
    for j in range(i):
        print(" ", end=" ")

    for k in range(i,n):
        if k == n - 1 or k == i :
            print("*", end=" ")
        else:
            print(" ", end=" ")




    print()


