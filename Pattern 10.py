n=int(input("Give your range :"))
for i in range(n):
    for j in range(i+1):
        print(" ",end= " ")
    for k in range(i,n):
        print("*",end= " ")
    for j in range(i+1,n):
        print("*",end= " ")
    print()
for i in range(n):
    for k in range(i,n):
        print(" ",end= " ")
    for j in range(i+1):
        print("*",end= " ")
    for j in range(i):
        print("*",end= " ")

    print()