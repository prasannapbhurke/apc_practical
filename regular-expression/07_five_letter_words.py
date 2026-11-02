import re

sentence = 'Every apple green plant grows fresh water drink clock apple'
five_letter_words = re.findall(r'\b[a-zA-Z]{5}\b', sentence)

print('Sentence:', sentence)
print('Five-letter words:', five_letter_words)
