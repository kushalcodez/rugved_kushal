#calculating no of words
s = input("enter for coleman liau:\n")
l = len(s)
wc = 1
sc = 1
lc = 1
for i in range(0,l):
    if(s[i].isalpha()):
        lc+=1
    if(s[i]==" "):
        wc +=1
    if(s[i] in ["!",".","?"]):
        sc += 1
print(f"word count {wc}\n")
print(f"sentence count {sc}\n")
print(f"letter count {l}\n")
S = sc/wc
L = lc/wc
cole = ((5.88 * L) - (29.6*S) - 15.8)
print(f"readablity index is : {cole}")