# This will print Hllo , skipping e
for i in "Hello":
    
    if i == "e":
        continue
    print(i, end = "")


# Just passes and do nothing
for i in range(10):
    if i % 3 == 0:
        pass
        print(i)


# List -- collection data type 
student = ["Maira", "Mithat", "Vasyl", True, 12, 13]

print(student[2:-1])
