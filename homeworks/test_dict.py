#lst_num = {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}

a = int(input("Give the number: "))
b = (a + 1)

for i in range(b): 
    if i == 0:
        continue
    c = str(i ** 2)
    lst = {i : c}
    print(lst)


# num = [i for i in range(a) if i == 0 continue lst = {i : i**2}]

# print(num)
# lst2 = [num**2 for num in range(10) if num %2 == 0] 
# print(lst2)



    


#Find the duplicates values in the dictionary

# sample_dict = {
#     'name1': 'John',
#     'name2': 'Alice',
#     'name3': 'Bob',
#     'name4': 'John',  # Duplicate value
#     'name5': 'Alice'  # Duplicate value
#     'name 6': 'Max'
# }

# for i in sample_dict.items():
#     if len(i) < 1:
#         print(i)
