
lst = [num for num in range(51) if num %2 == 0 ] 

print("Sum of all even numbers is: ",sum(lst))

lst2 = [num for num in range(51) if num %2 != 0]

print("Product of all odd numbers is: ", sum(lst2))

if [ sum(lst) > sum(lst2) ]:
    print("Even numbers are greather than odd")
else:
    print("Odd numbers are greater than even")

