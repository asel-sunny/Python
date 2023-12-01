def plusOne(digits):
    word = ""
    result = []

    for i in digits:
        word += str(i)

    num = int(word) + 1

    for i in str(num):
        result.append(int(i))

    return result

print(plusOne([9]))