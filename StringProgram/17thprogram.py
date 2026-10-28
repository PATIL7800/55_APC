s1 = input("First String: ")
s2 = input("Second String: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")