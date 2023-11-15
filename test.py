#print(123 + 456)

int1 = 12
int2 = 34

print(int1 + int2 )
print(int1 - int2)
print(int1 * int2)
print(int1 ** int2)
print(int1 / int2)
print(int1 // int2)
print(int1 % int2)

var = input("hello you: ")
print("hello", var)   # There has to be a comma or plus when calling variable in a print()
print("hello" + var)

var1 = input("first num: ")
var2 = input("second num: ")

print("This is the addition", var1 + var2) # This wont do addition but it will take as a string

var1 = int(input("Hello, give num : "))  # This will do math addition 
var2 = int(input("Hello, give second num : "))

print("This is the addition", var1 + var2)


var3 = float(input("Please provide a degree for celcius : "))

print(var3, "degree celcius would be ", var3 * (9/5) + 32)