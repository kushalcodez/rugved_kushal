def arraycheck (arr):
    n = len(arr)
    for i in range(n):
        for j in range (i+1,n):
            if (arr[i]==arr[j]):
                return arr[i],i
    return -1,-1

a = input("enter numbers")
ar1 = list(map(int,a.split()))
print(arraycheck(ar1))