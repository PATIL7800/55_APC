s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(set(freq.values()), reverse=True)

if len(values) >= 2:
    second = values[1]

    for ch in freq:
        if freq[ch] == second:
            print("Second most frequent character:", ch)
            break
else:
    print("No second most frequent character")