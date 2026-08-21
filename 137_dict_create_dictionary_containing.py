# Create a dictionary containing student names and marks. Calculate the average marks of all students.

students = {
    "Amit": 85,
    "Priya": 90,
    "Rahul": 78
}
avg = sum(students.values()) / len(students)
print("Average:", avg)
