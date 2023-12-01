def myfunc(x):
        if x == 0:
            return 1
        return x + myfunc(x -1)

print(myfunc(5))


# PRINTS Z
z = [1,2,3]

print(False or z)

print(17 % 7)

count = stages = "ff"

print(count)
print(stages)


print('A', 'B', sep='*')
print('C')


print('Alpha', end='')
print('Bravo')


print(4 -3 // 2 + 1)

maxValue = "skdn"
print(maxValue)

#264 = "sl"

print(1 // 2)

#print(264)

print(1 ** 2 / 2 // 3)


for i in range(2, -1, -2):
    print(i)

for i in range(1,1):
    print(i, end=' ')
else:
    print('FINISHED')


# break inside while
i = 1
while True:
    print(i, end=' ')
    i += 1
    print("test")
    if i == 3:
        break    
else:
    print('FINISHED')