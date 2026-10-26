import re

code_sample = '''
x = 10
# Full line comment
y = 20
url = "https://example.com"
'''

comments = re.findall(r'#.*', code_sample)

print('Code Sample:', code_sample)
print('Identified comments:', comments)
