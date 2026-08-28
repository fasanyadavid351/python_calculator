num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("enter the operation (+, -, *, /): ")

if operation == '+':
    print("the result is:", num1 + num2)
elif operation == '-':
    print("the result is:", num1 - num2)
elif operation == '*':
    print("the result is:", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("error division by zero not allowed")
    else:
        print("the result is:", num1 / num2)
else:
    print("Invalid operation")
