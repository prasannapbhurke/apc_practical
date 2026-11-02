import re

paragraph = 'Student: Aarav, Roll: 101, Marks: 85. Student: Diya, Roll: 102, Marks: 92. Student: Rohan, Roll: 103, Marks: 78.'

records = re.findall(r'Student:\s*([A-Za-z]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)', paragraph)

print('Paragraph:', paragraph)
print('\nExtracted Student Records:')
for name, roll, marks in records:
    print(f'Name: {name}, Roll No: {roll}, Marks: {marks}')
