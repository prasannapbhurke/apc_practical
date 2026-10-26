import re

sentence = 'This is is a test sentence with with duplicated repeated repeated words.'
pattern = r'\b(\w+)\s+\1\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)

print('Sentence:', sentence)
print('Consecutive repeated words found:', matches)
