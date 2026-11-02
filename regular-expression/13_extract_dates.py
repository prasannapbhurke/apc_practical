import re

paragraph = 'The project started on 15-08-2024 and completed on 26-10-2026. Next review on 05-01-2027.'
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', paragraph)

print('Paragraph:', paragraph)
print('Extracted Dates (DD-MM-YYYY):', dates)
