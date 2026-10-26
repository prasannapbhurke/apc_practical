import re

paragraph = 'Our head office is in Pune 411001, branch in Mumbai 400001, and Delhi center at 110001.'
pincodes = re.findall(r'\b[1-9]\d{5}\b', paragraph)

print('Paragraph:', paragraph)
print('Extracted 6-digit Indian PIN codes:', pincodes)
