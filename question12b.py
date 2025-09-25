N = int(input("enter no of rows"))
spaces = 2 * N - 1
stars = 0

#the outer loop will run for (2 * N - 1) times
for i in range(1, 2 * N):
    if i <= N:
        spaces = spaces - 2
        stars += 1
    else:
        spaces = spaces + 2
        stars -= 1
    for j in range(1, stars + 1):
        print("*", end="")
    for j in range(1, spaces + 1):
        print(" ", end="")
    for j in range(1, stars + 1):
        if j != N:
            print("*", end="")

    print() 