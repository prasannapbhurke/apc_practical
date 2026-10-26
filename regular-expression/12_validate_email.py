import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

emails = ['student@college.edu', 'user.name@gmail.com', 'bad_email@', 'wrong@.com', 'test@domain.org']

for e in emails:
    status = 'Valid' if validate_email(e) else 'Invalid'
    print(f'{e}: {status}')
