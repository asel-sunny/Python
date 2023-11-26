# Task 3

# Write a program that accepts user input of two variables, chars, and word. 
#The program should then perform the following tasks:


string1 = input("Please enter an even character string for the variable chars: ")
string2 = input("Please enter a word to insert into the middle of chars: ")

mid_index = len(string1) // 2
phrase = string1[:mid_index] + string2 + string1[mid_index:]

print(phrase)


