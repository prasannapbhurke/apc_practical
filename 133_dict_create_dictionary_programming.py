# Create a dictionary of programming languages and their creators. Display each key and value using a loop.

lang = {
    "Python": "Guido",
    "Java": "James",
    "C": "Dennis"
}
for k, v in lang.items():
    print(k, "-", v)
