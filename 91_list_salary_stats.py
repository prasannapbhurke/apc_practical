salary = [25000,35000,60000,52000,28000]
print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary)/len(salary))
above = 0
below = 0
for s in salary:
    if s > 50000: above += 1
    if s < 30000: below += 1
print("Above 50000:", above)
print("Below 30000:", below)

