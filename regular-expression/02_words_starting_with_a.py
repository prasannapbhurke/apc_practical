import re

sentence = 'An apple a day keeps anyone away, always active and alert.'
words = re.findall(r'\b[aA]\w*', sentence)

print('Sentence:', sentence)
print('Words beginning with A or a:', words)
