def ceaser(text):
    shift = 3
    res = []
    cl = list(text)
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            ec = chr((ord(char) - base + shift) % 26 + base)
            res.append(ec)
        else:
            res.append(char)
    final = "".join(res)
    return final

s = input("input text")
r = ceaser(s)
print(r)
