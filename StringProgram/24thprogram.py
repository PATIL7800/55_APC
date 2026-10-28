s = input("Enter string: ")

max_char = s[0]

for ch in s:
    if s.count(ch) > s.count(max_char):
        max_char = ch

print("Most Frequent:", max_char)