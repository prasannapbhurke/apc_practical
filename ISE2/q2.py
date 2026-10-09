import numpy as np

marks = np.array([85, 92, 78, 65, 88, 74, 90, 58])

average = marks.mean()

above_average = marks[marks > average]

print("Marks:", marks)
print("Average:", average)
print("Above average:", above_average)