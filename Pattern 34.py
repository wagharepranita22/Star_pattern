n = int(input("Give the value of n : "))
for i in range(n):
    for j in range(n):
        if i==0 or j == 0  or j == n-1 or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for k in range(i,n):
            print(" ",end ="")

    for k2 in range(i+1):
        print("*",end=" ")

    for k in range(i, n):
        print(" ", end="")

    for k2 in range(i+1):
        print("*",end=" ")


    print()