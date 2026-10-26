import re

text = 'Regular Expressions in Python are extraordinarily powerful and expressive.'
vowels = re.findall(r'[aeiouAEIOU]', text)

print('Input Text:', text)
print('Total Vowels Count:', len(vowels))
print('Vowels Found:', vowels)
