def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count
text = input("Enter a string:")
print( count_vowels(text))
