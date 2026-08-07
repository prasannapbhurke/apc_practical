names = ["Amit","Rahul","Priya"]
ages = [30,25,40]
names.append("Sneha")
ages.append(28)
index = names.index("Rahul")
names.pop(index)
ages.pop(index)
search = input("Enter patient name: ")
print("Patient Found" if search in names else "Patient Not Found")
for i in range(len(names)):
    print(names[i], ages[i])
print("Total Patients:", len(names))

