def checkifdiv(n, s):
    n2 = int(n)
    l = len(s)
    parts = []
    if l%n2 != 0 :
        return "non divisible string in n parts"
    
    pattern = s[:n2]
    for i in range(0,l,n2):
        part = s[i:i+n2]
        if(part != pattern):
            return "string sequences are not same"
        parts.append(part)
    return parts
    
n1 = input("enter n value")
s1 = input("enter string")
print(checkifdiv(n1,s1))
