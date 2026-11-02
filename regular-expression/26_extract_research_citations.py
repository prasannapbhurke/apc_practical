import re

references = '''
Smith, J. (2023). Deep Learning Foundations. doi:10.1016/j.jneumeth.2023.109845.
Contact: author.smith@ai-lab.edu. Available at: https://openalex.org/W1234567.
Gupta, R. (2025). Neural Optimization. doi:10.1145/3345678.9876543.
Reach out: r.gupta@institute.ac.in or visit http://arxiv.org/abs/2501.9999.
'''

dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', references)
years = re.findall(r'\b(19\d{2}|20\d{2})\b', references)
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', references)
urls = re.findall(r'https?://[^\s]+', references)

print('Extracted DOIs:', dois)
print('Extracted Publication Years:', list(set(years)))
print('Extracted Emails:', emails)
print('Extracted URLs:', urls)
