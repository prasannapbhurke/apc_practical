import re

text = 'Order 458 was placed on 12th August for 3 items costing 1499 rupees each.'
digits = re.findall(r'\d+', text)

print('Input Text:', text)
print('Extracted Digits:', digits)
