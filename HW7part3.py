# start
mesh: int = int(input("whats your number: "))
for i in range(1, mesh + 1,2):
    print(" " * (mesh - i), end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
for i in range(mesh - 2, -1, -2):
    print(" " * (mesh - i), end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# end