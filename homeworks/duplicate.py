#Find the duplicates values in the dictionary

sample_dict = {
    'name1': 'John',
    'name2': 'Alice',
    'name3': 'Bob',
    'name4': 'John',  # Duplicate value
    'name5': 'Alice',  # Duplicate value
    'name6': 'Max'
}

new_list = {}

for i in sample_dict.values(): 
    if i not in new_list:
        new_list.update(i)
        print(new_list)
    else:
    #print(i)
        print(i, "occured", i.count(), "times")
        #new_list[value].append(i)

#print(new_list)
# for i in sample_dict.values():
#    # print(i)
#     if sample_dict.values() == i:
#         print(i, "same")

#print(sample_dict.values)

# for i in sample_dict.values():
#     print(sample_dict.count(i))


    # dups = str(sample_dict)
    # if len(dups.count(i)) > 1:
    #     #dups.pop(i)
    #     print(i , "occured ", dups.count(i) ,  " times")
    # # dups2 = dups.count(i)
    # print(i, dups2)


#print(type(sample_dict))
