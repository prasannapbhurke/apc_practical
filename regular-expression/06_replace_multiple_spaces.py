import re

text = 'Python    is    a    very      popular    programming   language.'
cleaned_text = re.sub(r'\s+', ' ', text).strip()

print('Original Text:', text)
print('Cleaned Text:', cleaned_text)
