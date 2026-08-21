# Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

students = {
    "Amit": 85,
    "Priya": 90,
    "Rahul": 78
}
top = max(students, key=students.get)
print("Highest:", top, students[top])
