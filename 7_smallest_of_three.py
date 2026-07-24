#Write a PYTHON program to find a smallest of three numbers
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Three Number: "))

if(number1<number2 and number1<number3 ):
    print("First number is Smaller")
elif(number2<number1 and number2<number3):
    print("Second Number is Smaller")
else:
    print("Third Number is Smaller")

