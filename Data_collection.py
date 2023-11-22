# List -- collection data type
student = ["Maira", "Mithat", "Vasyl", True, 12, 13]

print(student[2:-1])

student.append("Guliza")  # append will always append to the back of the list
  

student.insert(2, "Guliza") # (index, value) , will add Guliza in the 2 index of the list

print(student)

# for name in student:
#     print(name[0])   # it will print only the first letter of every word since it itterates through each word


# Giving the sum of all numbers in lst 
lst = [10, 20, 30]
sum = 0

for i in lst:
    sum = i + sum

print(sum)


# Prints the sum of odd and even numbers
lst = [10, 21, 32, 40, 33, 22,45, 78, 90]

odd = 0
even = 0

for i in lst:
    if i%2 != 0:
        odd = i + odd
    else:
        even = i + even

print("These are odd ", odd)
print("These are even ", even)


# SORT FUNCTION

lst.sort()  # sorts with smallest to greatest
lst.sort(reverse=True)  # reversed the numbers 

print(lst )  # saves the value from the latest sort

print(sorted(lst))  # sorted function used in print function because it doesnt save the original value, but it prints only in print
print(sorted(lst, reverse=True)) 


# Complicated print
lst = ["string", 11, [1,["hello", "world"], 2, 3]]
print(lst[-1][1][0])   # prints hello , starting from -1 which is the list from end and goes by logic

lst2=lst
del lst[2]  # deletes 2nd index from lst
print(lst)  # it will print the deleted 2nd index list even though you defined lst2=lst before del .. It saves the latest value to memory

lst = ["string", 11, [1,["hello", "world"], 2, 3]]
lst2=lst
lst3=lst[::]  # it will print the original value of lst , because its taking every value of index 

lst2 = lst.copy() # again this will take a hard copy of the original value

print(lst2)


lst4 = [1, 2, 3, 4]
lst4[0] = 10

print("Mutable ----", lst4)

# POP FUNCTION
lst4.pop() # removes from the end of the list , same thing as del or you can give lst4.pop(2)

# INDEX FUNCTION
#lst4.index(4)
#print(lst4)

# COUNT FUNCTION 
print(lst.count(5))  # it will look for duplicates and print how many times of 5 you have in the list


# IMMUTABILITY : Strings, tuple, bool, floats, int are immutable
# List, dictionaries : mutable


# LIST COMPREHENSION

lst = []

for i in range(10):
    if i %2 == 0:
        lst.append(i)
print(lst)

lst2 = [num for num in range(10)]
print(lst2)

lst2 = [num for num in range(10) if num % 2 == 0]
print(lst2)

lst2 = [num**2 for num in range(10) if num %2 == 0] 
print(lst2)

tupl = tuple(num for num in range(10) if num %2 == 0)
print(tupl)


# TUPLES

a = ("some text")
print(type(a))





    
    