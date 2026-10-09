from employee.salary import calculate as calc_salary
from employee.tax import calculate as calc_tax
from employee.bonus import calculate as calc_bonus

salary = calc_salary(50000, 10000, 5000)
tax = calc_tax(salary)
bonus = calc_bonus(salary)

print("Salary:", salary)
print("Tax:", tax)
print("Bonus:", bonus)