# Write a Python script to print a dictionary where the keys are numbers and the values are the square of the keys.
#take an input from a user until which number it should take


a = int(input("Give the number: "))
b = (a + 1)

for i in range(b): 
    if i == 0:
        continue
    c = str(i ** 2)
    lst = {i : c}
    print(lst)