# solution 1
n=int(input("Give your range :"))
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end= " ")
    print()
# solution 2
for i in range(n):
    for j in range(i,n):
        print("*",end= " ")
    print()