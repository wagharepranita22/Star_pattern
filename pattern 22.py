n=int(input("Give your range : "))
for i in range (n):
    for j in range (n):
        if j == 0 or j == n-1:
            print("*", end=" ")

        print(" ", end=" ")
    print()