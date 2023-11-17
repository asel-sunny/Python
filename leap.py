year = int(input("Enter a year: "))


first = (year / 100)
second = (year / 400)
# If the remainder is 0 

if first%2 == 0 & second%2 == 0:
    print("leap")
else:
    print("not leap")





    