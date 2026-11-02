import re

text = 'Line 1\tTabbed text\nLine 2 with spaces  and newline\n'
spaces = re.findall(r' ', text)
tabs = re.findall(r'\t', text)
newlines = re.findall(r'\n', text)

print('Text Representation:', repr(text))
print('Space characters count:', len(spaces))
print('Tab characters count:', len(tabs))
print('Newline characters count:', len(newlines))
