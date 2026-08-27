# Given two dictionaries, identify the values that are common to both dictionaries.

# Program: Dict Given Two Dictionaries
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 5, "d": 3}
common = d1.values() & d2.values()
print(common)
