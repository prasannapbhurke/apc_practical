# Create a dictionary containing employee information and display the value associated with a specified key.

employee = {
    "E101": "Amit",
    "E102": "Priya",
    "E103": "Rahul"
}
key = input("Enter key: ")
print(employee.get(key, "Not Found"))
