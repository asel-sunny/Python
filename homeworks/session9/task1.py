# Create a function that takes 2 list arguments. 
# The function is supposed to merge both of the lists together and return a sorted list.


lst = [1,2,6,3,7,4]
lst2 = [66,34,9,76]

lst.extend(lst2)
print(sorted(lst))