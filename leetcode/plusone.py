#This wont work with 9  

digits = [9]

# new = digits[-1] + 1

# print(digits)

# last = digits[-1] + 1
# new = digits[:-1] + last

#digits[-1] = digits[-1] +1


if len(digits) < 2 or digits == "9":
    digits[-1] = digits[-1] +1
    a = str(digits)
    #b = []
    #b.append(a)
    print(a)
    #print(list(digits))
else:
    digits[-1] = digits[-1] +1
    print(digits)
    
#print(len(digits))


# s = 10
# a = str(s)
# c = []

# for i in a:
#     c.append(i)

# print(c)