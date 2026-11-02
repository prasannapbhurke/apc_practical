import re

text = 'Visit our site at https://www.google.com or documentation at http://python.org/docs for details.'
urls = re.findall(r'https?://[\w\.-]+(?:/[\w\.-]*)*', text)

print('Input Text:', text)
print('Extracted Web Addresses:', urls)
