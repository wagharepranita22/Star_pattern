# pyramid star pattern
n = int(input("Give your range  :"))
for i in range(n):
    for j in range(i, n-1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i, n-1):
        print(" ", end="")


    for j in range(i, n-1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i, n-1):
        print(" ", end="")


    print()