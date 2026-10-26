import re

text = 'Hello @World! Python #123 is *awesome* & fun to (learn)...'
cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', text)

print('Original Text:', text)
print('Cleaned Text:', cleaned)
