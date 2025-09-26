def hillno(num):
    
    digits = str(abs(num))
    n = len(digits)
    
    if n <= 2:
        return True
    peak = 0
    while peak < n - 1 and digits[peak] <= digits[peak + 1]:
        peak += 1
    
    for i in range(peak, n - 1):
        if digits[i] <= digits[i + 1]:
            return False
    
    return peak > 0 
a = int(input("enter number     "))
print(hillno(a))