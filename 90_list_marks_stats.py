marks = [60,70,80,90,55,76,88,91,45,66,77,81,69,58,92,73,84,62,79,68]
highest = max(marks)
lowest = min(marks)
average = sum(marks)/len(marks)
above = 0
below = 0
for m in marks:
    if m > average: above += 1
    elif m < average: below += 1
print(highest, lowest, average, above, below)

