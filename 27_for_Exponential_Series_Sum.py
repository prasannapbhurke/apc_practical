n = int(input("Enter an integer (n): "))

total_sum = 0
fact = 1

for i in range(n + 1):
    if i == 0:
        fact = 1
    else:
        fact *= i
    total_sum += 1 / fact

print(total_sum)