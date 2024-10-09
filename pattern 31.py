n=int(input("Give your  n value : "))
for i in range (n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i+1):
        if k == 0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for k in  range(i+1):
        if k == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range (n) :
    for j in range(i):
        print(" ",end=" ")
    for k in range (i,n):
        if i == k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(i,n):
        if k == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()