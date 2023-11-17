import re

password = input("Give password: ")



# for i in passw:
#     if len(passw) > 8 and i.isupper() and i.islower() and i.isdigit():
#         print("it has")
# if passw.isupper():
#     print("it has")

# for i in passw:
#     if len(passw) > 8 and i.isupper():
#         if i.islower() and i.isdigit():
#             print("it has print")
#         fi
#     fi

# for i in passw:
#     re.search(r'[0-9]', i)

    
# A sample regular expression to find digits.  
# regex = '\d+'             
    
# match = bool(re.findall(regex, passw))  
# # print(match)

# if match is True:
#     if 

# if re.findall(regex, passw) = True:
#     print("it has nums ")
 

# caps = re.compile(r'[A-Z]')
# #pattern.match(passw)
# small = re.compile(r'[a-z]')
# num = re.compile(r'\d')


# if bool(caps.match(passw)) == True:
#     if bool(small.match(passw)) == True:
#         print("matches all for now")

       # if bool(num.match(passw)) == True:


# for i in passw:
#     if bool(re.search(r'[0-9]', i)) == True:
#         for a in passw:
#             if bool(re.search(r'[a-z]', a)) == True:
#                 for b in passw:
#                     if bool(re.search(r'[A-Z]', b)) == True:
                        
#                         print("matching")



############### GOOGLE IS MY BEST FRIEND !!!!! ################## 
flag = 0
while True:
    if (len(password)<=8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]" , password):
        flag = -1
        break
    elif re.search("\s" , password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
 
if flag == -1:
    print("Not a Valid Password ")



       