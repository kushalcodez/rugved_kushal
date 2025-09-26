def fibonacci(n):
    if(n<0):
        return "Error non negative"
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n1 = input("enter no for fibonacci sum")
n2 = int(n1)
print(fibonacci(n2))
