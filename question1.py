def istrue(a , b ,c ):
    return a and b and c
#for true check

print("input 3 values true false 0 1 \n")
v1=input("1st value\n").strip().lower()
v2=input("2nd value\n").strip().lower()
v3=input("3rd value\n").strip().lower()
def cb(value):
    if(value in ["true","1"]):
        return True
    elif(value in ["false","0"]):
        return False

b1 = cb(v1)
b2 = cb(v2)
b3 = cb(v3)
res = istrue(b1,b2,b3)
print(res)