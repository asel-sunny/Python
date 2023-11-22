d = {"a" : "hello", "s" : "something", "f" : True, "int" : 180}
c = {10 : "hello2"}

# a is key while hello is value

print(d["s"]) # will print something
print(d["a"] , c[10])  # will print hello hello2

for i in d.values():   # iterating through values of keys 
    print(i)

for i in d.keys():   # iterating through keys
    print(i)

for i in d.items():  # iterating through keys and values and will show tuple data type
    print(i)


d["s"] = "anything"   # will replace something to anything , so its mutable object
d["f"] = False   # changing True to False
print(d)

d.update({"lst" : [1,2,3,4]})  # appending new list in dictionary
print(d)

d.pop("a")   # it will remove "a" key:value
print(d)

del d["s"]   # removes "s" key:value .. same as pop 
print(d)





