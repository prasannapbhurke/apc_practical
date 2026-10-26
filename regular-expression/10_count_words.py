import re

sentence = 'Data Science, Machine Learning, and AI are transforming industries today.'
words = re.findall(r'\b\w+\b', sentence)

print('Sentence:', sentence)
print('Words List:', words)
print('Total Word Count:', len(words))
