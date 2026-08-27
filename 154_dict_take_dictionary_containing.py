# Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

# Program: Dict Take Dictionary Containing
students = {
    "Amit": "CSE",
    "Priya": "IT",
    "Rahul": "CSE",
    "Sneha": "ECE"
}
dept_groups = {}
for name, dept in students.items():
    if dept not in dept_groups:
        dept_groups[dept] = []
    dept_groups[dept].append(name)
print(dept_groups)
