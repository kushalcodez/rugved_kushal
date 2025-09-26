
n1 = input("enter number till fibonacci sequence")
n2 = int(n1)
a = 0
b = 1
next = b  
count = 1

while count <= n2:
    print(next, end=" ")
    count += 1
    a = b
    b = next
    next = a + b
