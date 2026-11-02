import re

def validate_mobile(number):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

test_numbers = ['9876543210', '8123456789', '5123456789', '987654321', '98765432100']

for num in test_numbers:
    status = 'Valid' if validate_mobile(num) else 'Invalid'
    print(f'{num}: {status}')
