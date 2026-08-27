# Given a list of numbers, create a dictionary containing each unique number and its frequency.

# Program: Dict Given List Numbers
nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print(freq)
