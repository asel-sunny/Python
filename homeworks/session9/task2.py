int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation != "/" or int2 != 0:
   for i in operation:
        if i == "+":
            print(int1 + int2)
        elif i == "-":
            print(int1 - int2)
        elif i == "*":
            print(int1 * int2)
        elif i == "/":
            print(int1 / int2)
else:
    print("You cant divide by 0")
