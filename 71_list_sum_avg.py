numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

total = sum(numbers)
avg = total / len(numbers)

print("Sum:", total)
print("Average:", avg)