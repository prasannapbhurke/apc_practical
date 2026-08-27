# Create a dictionary containing employee names and salaries. Find:
# Highest salary
# Lowest salary
# Average salary
# Employees earning more than ₹50,000

# Program: Dict Create Dictionary Containing
salary = {
    "Amit": 60000,
    "Priya": 55000,
    "Rahul": 28000,
    "Sneha": 75000
}
print("Highest:", max(salary, key=salary.get), max(salary.values()))
print("Lowest:", min(salary, key=salary.get), min(salary.values()))
print("Average:", sum(salary.values()) / len(salary))
above = [k for k, v in salary.items() if v > 50000]
print("Above 50000:", above)
