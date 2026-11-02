import re

sentence = 'The students always focus on books, sports, and discussions.'
words = re.findall(r'\b\w+[sS]\b', sentence)

print('Sentence:', sentence)
print('Words ending with s:', words)
