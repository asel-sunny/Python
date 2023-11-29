# Recursion -- function call itself inside of the function
#  - Dangerous if you dont understand what you are doing 


def someFunct(name, age):
   # someFunct():
    return f"Hello {name} , your age is {age}"


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

print(fact(5))