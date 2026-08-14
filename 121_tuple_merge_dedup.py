t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
merged = t1 + t2
unique = ()
for i in merged:
    if i not in unique:
        unique += (i,)
print(unique)

