# name1 = "hello"
# print(name1[10])

# Try / Except used for error handling 

errors = (IndexError, ArithmeticError, TypeError)
try:
    name = "hello" 
    name[0] = 'n'
    print(name[10])
except errors:
    print("you are trying to get an index which is out of range")
# except TypeError: 
#     print("Type error")   # so you can define multiple exceptions and based on error , it will go to correct exception type

finally:    # will run no matter what , no matter if exception or not
    print("Finally keyword")   

