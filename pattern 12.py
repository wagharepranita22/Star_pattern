n=int(input("Give the range  : "))
for i in range(n):
    for j in range(i,n):
        print(" ",end= " ")
    for j in range(i+1):
        print(9,end= " ")
    for j in range(i,n):
        print("",end= " ")
    print()