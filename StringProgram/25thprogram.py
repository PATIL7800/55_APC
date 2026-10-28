s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) > 1:
    print("Second Most Frequent:", sorted_freq[1][0])