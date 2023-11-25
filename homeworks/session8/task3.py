#from collections import Counter


animal_list = ['lion', 'tiger', 'lion', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']


new_set = set(animal_list)

for i in new_set:
    count = animal_list.count(i)
    res = {i:count}
    print(res)
   



# for index, i in enumerate(animal_list):
#     if i not in uniq_list:
#         uniq_list.append(i)
#         #print(uniq_list)
#     else:
#         seen.add(i)
#         count = animal_list.count(seen) + 1
#         #seen.add(i)
#         print(seen , count)

# new = []
# count =0 
# for i in animal_list:
#     uniq_list.append(i)
#     if seen in uniq_list:
#         seen.add(i)
#         count =  animal_list.count(i)
# print(seen, "occured", count, "times")

    # if i not in uniq_list:
    #     uniq_list.append(i)
    #     #print(uniq_list)
    # else:
    #     seen.add(i)
        
    #     print(seen, "occured", count, "times")
    #     continue
        # count =  animal_list.count(i)
        # print(seen, "occured", count, "times")
        
       # count = count +1
        # e= set(seen.append(i))
        # #new_list = seen.append(i), animal_list.count(i)
        # print(e)
        

#print(seen)


# x = set()
# count = 0

# for i in animal_list:
#     # if i in uniq_list:
#     #     x.add(i)
#     #     count =count+1
#         # if i == x:
#         #     count = count +1
# # print(x)

#     if (i == x):
#         count = count + 1
#         x.add(i)
# print(x , count)


# for index, i in enumerate(animal_list):
#     if i not in uniq_list:
#         uniq_list.append(i)
#         #print(uniq_list)
#     else:
#         seen.add(i)
        
#         print(seen, "occured", i.count(str(seen)))
        
        #print(seen)

    #print(index, i)
# dups = []
# seen = set()

# for i in animal_list:
#     if i in seen:
#         dups.append(i)
#         print(dups)
    

# seen = set()
# dupes = [x for x in animal_list if x in seen ] 
# print(dupes)

# seen = set()
# for i in animal_list:
#     if i in seen.add(i):
    
#         print(seen)