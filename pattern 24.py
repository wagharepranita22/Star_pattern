n=int(input("give n value : "))
for i in range (n):
    for j in range (n):
        if i==j:
            print("*",end=" ")
        else:
            if j+i==n-1:
                print("*", end=" ")
        print(" ",end = " ")
    print()