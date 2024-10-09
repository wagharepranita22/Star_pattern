n = int(input('Give your n value  : '))
for i in range(n):
        for k in range(i):
            print(" ",end=" ")
        for j in range(i,n):
            if i == 0 or i == j :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        for j in range(i+1, n):
            if i == 0 or j == n-1 :
                print("*", end=" ")
            else:
                print(" ",end =" ")
        print()
for i in range(n):
    for j in range (i,n-1):
        print(" ",end=" ")
    for k in range (i):
        if k==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end =" ")

    for j in range(i+1):
        if i == j or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()