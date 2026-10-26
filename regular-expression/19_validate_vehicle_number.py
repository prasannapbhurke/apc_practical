import re

def validate_vehicle(num):
    pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$'
    return bool(re.match(pattern, num))

vehicles = ['MH12AB1234', 'DL01A9999', 'KA05MC7777', 'MH-12-1234', '12MHAB1234']
for v in vehicles:
    status = 'Valid' if validate_vehicle(v) else 'Invalid'
    print(f'{v}: {status}')
