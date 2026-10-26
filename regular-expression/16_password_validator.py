import re

def validate_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r'[A-Z]', pwd):
        return False
    if not re.search(r'[a-z]', pwd):
        return False
    if not re.search(r'\d', pwd):
        return False
    if not re.search(r'[@$!%*?&#]', pwd):
        return False
    return True

passwords = ['Admin@123', 'weakpass', 'NO_DIGIT!', 'NoSpecial123', 'SuperSecret#99']
for p in passwords:
    status = 'Strong & Valid' if validate_password(p) else 'Invalid'
    print(f'{p}: {status}')
