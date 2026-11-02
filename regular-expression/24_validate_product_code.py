import re

def validate_product_code(code):
    pattern = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'
    return bool(re.match(pattern, code))

codes = ['ABC-1234-XY', 'XYZ-9999-AB', 'AB-1234-XY', 'ABC-123-XY', 'ABC-1234-X1']
for c in codes:
    status = 'Valid' if validate_product_code(c) else 'Invalid'
    print(f'{c}: {status}')
