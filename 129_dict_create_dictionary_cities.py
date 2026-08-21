# Create a dictionary of cities and their populations. Remove a specified city from the dictionary.

cities = {
    "Pune": 3100000,
    "Mumbai": 12400000,
    "Delhi": 11000000
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
print(cities)
