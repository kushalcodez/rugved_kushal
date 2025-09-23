#luhns algo
def luhns(cc):
    cc2 = str(cc).replace(' ', '')
    cc2 = cc2[::-1]
    cc2 = [int(x) for x in cc2]
    checksum = 0
    for i in range (0,len(cc2),2):
        cc2[i]*=2
        if cc2[i] > 9:
            cc2[i] = cc2[i]%10+1
    checksum = sum(cc2)
    
    return checksum % 10 == 0


number = input("enter a credit card number")
print(luhns(number))
