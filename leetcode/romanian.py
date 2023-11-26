# Dont know how to give 4 , 9 .. 

roman = input("give romanian num :" )

ones = []
fours = []
fives = []
nines = []
tens = []
fifty = []
fivehundred = []
thousand = []
#otal = 


for i, x in enumerate(roman):
    if x == "I":
        ones.append(1)
    elif x == "V":
        fives.append(5)
    elif x == "X":
        tens.append(10)
    elif x == "L":
        fifty.append(50)
    elif x == "D":
        fivehundred.append(500)
    elif x == "M":
        thousand.append(1000)
    
print(sum(ones + fives + tens + fifty + fivehundred + thousand))



# for i, x in enumerate(roman):
#     if "I" in roman:
#         ones.append(1)
#     elif "V" in roman:
#         fives.append(5)
#     elif "X" in roman:
#         tens.append(10)

# print()
        

# if s == "I":
#     one = 1
#     print(one)
#     # for i in range(3)
#     # i = i