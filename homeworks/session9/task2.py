int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")


if operation == "+":
    print(int1 + int2)
elif operation == "-":
    print(int1 - int2)
elif operation == "*":
    print(int1 * int2)
elif operation == "/":
    print(int1 / int2)