import re

post = 'Celebrating innovation! #AI #PythonProgramming #Tech2026 is trending. #DevLife!'
hashtags = re.findall(r'#\w+', post)

print('Post Content:', post)
print('Extracted Hashtags:', hashtags)
