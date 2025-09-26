def rotate_and_display():
    n = int(input("Enter the size of the matrix (n x n): "))
    print(f"Enter {n} rows with {n} space-separated integers each:")
    matrix = [list(map(int, input().split())) for k in range(n)]

    
    rotated = [[0] * n for _ in range(n)]
    #initializing with zeros
    
    for j in range(n):
        for i in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    print("\nRotated Matrix (90° Clockwise):")
    for row in rotated:
        print(" ".join(map(str, row)))

rotate_and_display()
