#Find the duplicates values in the dictionary

sample_dict = {
    'name1': 'John',
    'name2': 'Alice',
    'name3': 'Bob',
    'name4': 'John',  # Duplicate value
    'name5': 'Alice',  # Duplicate value
    'name6': 'Max'
}

for i in sample_dict.values():
    
    dups = str(sample_dict)
    if len(dups.count(i)) > 1:
        #dups.pop(i)
        print(i , "occured ", dups.count(i) ,  " times")
    # dups2 = dups.count(i)
    # print(i, dups2)


#print(type(sample_dict))
