year = int(input("Enter a year: "))


# first = (year / 100)
# second = (year / 400)
# If the remainder is 0 

# if ((year%4 == 0 and year%400 == 0) or (year%400 == 0 and year%100 == 0)):
#     print("leap")
# else:
#     print("not leap")



# if year%4 == 0 and (year%100 == 0 and year%400 != 0):
#     print("leap")
# else:
#     print("not leap")

year1 = year[2:3]
if year2%4 == 0:
    print("leap")
elif year%100 == 0 and year%400 != 0:
    print("leap")
else:
    print("not leap")