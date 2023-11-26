
lst = [num for num in range(51) if num %2 == 0 ] 

print("Sum of all even numbers is: ",sum(lst))

lst2 = [num for num in range(51) if num %2 != 0 ]

result = 1
for x in lst2:
    result = result * x
print("Product of all odd numbers is: ", result)


if  sum(lst) > result :
    print("Even numbers are greater than odd")
else:
    print("Odd numbers are greater than even")

