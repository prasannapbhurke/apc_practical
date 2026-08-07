scores = [45,60,120,30,99,105,75,15,130,80]
print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores)/len(scores))
century = 0
half = 0
for s in scores:
    if s >= 100: century += 1
    elif s >= 50: half += 1
print("Centuries:", century)
print("Half-centuries:", half)

