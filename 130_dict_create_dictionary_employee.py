# Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.

emp = {
    101: "Amit",
    102: "Priya",
    103: "Rahul"
}
eid = int(input("Enter employee ID: "))
print("Exists" if eid in emp else "Not Found")
