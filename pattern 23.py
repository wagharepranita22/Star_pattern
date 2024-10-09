n = int(input(" Give your n value :  "))
for i in range (n):
    for j in range (n):
        if (i == n//2 ) :
            print("+", end=" ")
        else:
            if (j == n//2):
                print("+",end=" ")
            print(" ",end = " ")
    print()


