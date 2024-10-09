n= int(input('Give your n value  : '))
for i in range(n):
        for j in range(i,n):
            if (j == n-1 or i == j or i == 0 ) :
                print("*", end=" ")
            else:
                print(" ",end =" ")

        for j in range(i):
            print(" ",end=" ")
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n):
            if j == n-1 or j == i or i == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()

for i in range (n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print("*",end=" ")
        else:
            if i == n // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    for j in range(n):
        if i == 0 or j == n-1 or i == n-1:
            print("*",end=" ")
        else:
            if i == n // 2 :
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()


for i in range (n):
    for j in range (i+1):
        if i == n-1 or j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(i,n-1):
        print(" ",end=" ")

    for j in range(i, n-1):
        print(" ", end=" ")

    for j in range(i+1):
        if i == n - 1 or i == j or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


