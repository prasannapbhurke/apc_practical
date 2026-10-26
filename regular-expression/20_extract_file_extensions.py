import re

text = 'Here are the deliverables: report.pdf, project_code.py, raw_data.csv, and photo.jpeg.'
extensions = re.findall(r'\.[a-zA-Z0-9]+', text)

print('Text:', text)
print('Extracted Extensions:', extensions)
