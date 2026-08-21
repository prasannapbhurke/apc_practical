# Create a dictionary containing student marks. Update the marks of a specified student.

students = {
    "Amit": 85,
    "Priya": 90,
    "Rahul": 78
}
name = input("Enter name: ")
marks = int(input("Enter new marks: "))
students[name] = marks
print(students)
