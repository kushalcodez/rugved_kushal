s = input("input string")
cl = list(s)
n = len(cl)
for i in range(n):
    ind=i
    for j in range(i+1,n):
        if (cl[j]<cl[i]):
            ind = j
    temp = cl[i]
    cl[i]=cl[ind]
    cl[ind]=temp

s2 = "".join(cl)
print(s2)
