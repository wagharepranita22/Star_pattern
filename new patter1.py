n = int(input("Give your n th : "))
for i in range(n):
    for j in range(i):
        for k in range(n):
            print("*",end=" ")
    print()
