import re

text = 'The Quick Brown FOX Jumps Over The Lazy DOG.'
uppercase_letters = re.findall(r'[A-Z]', text)

print('Input Text:', text)
print('Uppercase Letters:', uppercase_letters)
