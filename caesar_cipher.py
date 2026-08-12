s = input("Enter a message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch.isalpha():
        result += chr((ord(ch.lower()) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted message:", result)