s = input("enter string")
ns = sorted(s)
print(ns)
set1 = set(ns)
for element in set1:
    count=0
    for character in ns:
        if character == element:
            count +=1
    print(f"count of '{element}' is '{count}'.")
