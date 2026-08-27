# Given two dictionaries, find the keys that are common to both dictionaries.

# Program: Dict Given Two Dictionaries
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 5, "d": 6}
common = d1.keys() & d2.keys()
print(common)
