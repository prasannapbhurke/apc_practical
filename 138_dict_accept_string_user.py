# Accept a string from the user and create a dictionary containing each character and its frequency.

s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
