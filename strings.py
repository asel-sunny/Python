string = "hello world"

#STRING SLICING 
print(string[1]) #prints e , starts count from start by 0 taking each letter
print(string[-1]) # prints o , counts from end 
print(string[0:5]) # prints hello , counts from 0 to 5 
print(string[-5:]) # prints world , counting from the end till end of string
print(string[6:]) # prints world , counting from start till end till end of string


text = "The mesmerizing sunset something warm tranquil and beach"

print(text[4:15])
print(text[-5:])
print(text[-18:-10])
print(text[16:])

#sep and end are built in variables within the print function .. sep is separator and end is printing end
print("hello", text, "this is hello again", sep=" || ", end=" |||| This is end") 