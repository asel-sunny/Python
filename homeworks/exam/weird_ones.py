numbers = [4,3,2,1]
print(numbers[numbers[3]])  # will take first index output numbers[3] = 1, and put it in next index output
                            # which is numbers[1] = 3 

print(numbers[3:5])  # will print [1], the most important is start point cant be out of range index
print(numbers[5])  # out of range error 
print(numbers[5:])  # empty []
print(numbers[3:3]) # empty []
print(numbers.index(1))  # prints the index number of 1 which is 3

def f():
    t = {"One": "gh", "TV": "kd", "age": "hy"}  
    for i in t.values():
        print(i[0],end="")
f()   # this function prints 0 index of each value in a dictionary
