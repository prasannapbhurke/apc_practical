patients = ((1, "Amit", 30, "A+"), (2, "Rahul", 25, "B+"))
for p in patients:
    print(p)
search_id = int(input("Enter ID: "))
for p in patients:
    if p[0] == search_id:
        print("Found")
print("Total:", len(patients))

