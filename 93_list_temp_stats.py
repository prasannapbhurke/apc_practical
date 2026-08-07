temp = [30,32,31,29,35,36,34,33,32,31]
print("Hottest:", max(temp))
print("Coldest:", min(temp))
avg = sum(temp)/len(temp)
above = 0
below = 0
for t in temp:
    if t > avg: above += 1
    elif t < avg: below += 1
print("Average:", avg)
print("Above Average:", above)
print("Below Average:", below)

