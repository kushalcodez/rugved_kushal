#anagram
s1 = input("enter first string")
s2 = input("enter second string")
c1 = sorted(s1.lower())
c2 = sorted(s2.lower())
if c1 == c2:
    print("they are anagrams of each other")
else:
    print("they are not anagrams of each other")