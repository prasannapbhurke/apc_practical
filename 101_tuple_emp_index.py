emp_ids = (101, 102, 103, 104)
id = int(input("Enter ID: "))
print(emp_ids.index(id) if id in emp_ids else "Not Found")

