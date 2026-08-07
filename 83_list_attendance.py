students = ["Amit","Rahul","Priya"]
print("Total:", len(students))
name = input("Search student: ")
print("Present" if name in students else "Absent")
students.append("Sneha")
students.remove("Rahul")
print(students)

