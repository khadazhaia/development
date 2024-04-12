import random

'''Create a new list that contains any students without the letter a, do one version with a for loop, do another one with list comprehension'''

# For Loop
students = ['Anna', 'Dana', 'Sarah', 'Farley', 'Oleg', 'Gionni', 'Brenetta']
# for s in students:
#     if "a" not in s:
#         print(s)

# List Comprehension - new_list = [x for x in original_list if condition]
students = ['Anna', 'Dana', 'Sarah', 'Farley', 'Oleg', 'Gionni', 'Brenetta']
new_students = [s for s in students if "a" not in s]
# print(new_students)


''' Create a list with 1 added to each item in the list, do one version with a for loop, do one with list comprehension'''

original_list = [1, 2, 3, 4, 5, 6]

# Creating an empty lst
new_list = list()

# Loop through and add +1 to evry item as we iterate through
for o in original_list:
    new_list.append(o + 1)
# print(new_list)


# List Comprehension - new_list = [expression for x in original_list]
new_list = [new_list.append(o + 1) for o in original_list]
# print(new_list)


''' Ranges '''

# for o in range(len(original_list) + 1):
#     if o == 0:
#         continue
#     new_list.append(o + 1)
#     new_list.remove(None)
# print(new_list)


'''
Create the following output from the following two lists

software = ['Word', 'Excel', 'Powerpoint', 'Access']
purpose = ['word processing', 'spreadsheet', 'presentation', 'database']

Word is word processing software.
Excel is spreadsheet software
Powerpoint is presentation software
Access is database software

'''

software = ['Word', 'Excel', 'Powerpoint', 'Access']
purpose = ['word processing', 'spreadsheet', 'presentation', 'database']


# With ranges

# for s in range(len(software)):
#     print(f'{software[s]} is {purpose[s]}')


# With zip
# for s, p in zip(software, purpose):
#     print(f'{s} is {p} software')


'''
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list those numbers.

# Try the split string method
'''

# list = []

# user_input = input("Enter a sequence of comma-separated numbers: ").split(",")
# print(user_input)

# or

# user_input = input("Enter a sequence of comma-separated numbers: ")
# result = user_input.split(",")
# print(result)

'''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''

color_list = ["Red","Green","White","Black"]
# print(f'The first color is {color_list[0]} and the last color is {color_list[-1]}')


'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
5 + 55 + 555 = 615
Expected Result : 615
'''
# num1 = "5"
# num2 = "5"
# result = num1 + num2
# print(result)

# userinput = input("Please enter your number: ")

# first = int(userinput) # 5
# second = int(userinput + userinput) # (userinput * 2) 55
# third = int(userinput + userinput + userinput) # (userinput * 3) 555 

# result = first + second + third
# print(result)


'''
Using a for loop and a conditional, write a Python program that concatenates all elements in a list into a string.

my_list = [1, 2, 3, 4, 5]
new_string = '12345'
'''
my_list = [1, 2, 3, 4, 5]
new_string = " "

# for m in my_list:
#     m = str(m) # changes integer to string
#     if m not in new_string:
#        new_string += m
# print(new_string)


'''
Write a Python program to sum the first n positive integers..

Example: 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

Example: 4
1 + 2 + 3 + 4 = 10

Example 5
1 + 2 + 3 + 4 + 5 = 15

'''

# n = int(input('Enter a number: '))
# sum = 0

# for r in range(n + 1): # all the numbers need to add up
#     sum += r
    
# print(sum)


'''  Write a Python program to calculate sum of digits of a number. '''

# user_input = input('Enter a number: ')

# sum = 0

# for u in user_input:
#     sum += int(u)

# print(sum)




''' More exercises'''

''' Write a Python program to add two objects if both objects are integers.
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
'''

obj_1 = 432
obj_2 = 6

# print(isinstance(obj_1, int))

# print(isinstance(obj_2, int))

# if isinstance(obj_1, int) and isinstance(obj_2, int):
#     print(obj_1 + obj_2)
# else:
#     print("sorry you can only add two numbers")

''' Write a Python program to test whether all numbers in a list are greater than a certain number.
num = 5

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
num = 5

list = [6, 7, 8, 9, 10]


# if all(l > num for l in list):
#         print(True)
# else:
#     print(False)



''' Write a Python program to count the number of occurrences of a specific character in a string.  Solve it with a string method as well as a for loop
char = 'i'
word = 'supercalifragilisticexpialidocious'
'''
# string method

char = 'i'
word = 'supercalifragilisticexpialidocious'

# spec_char = word.count(char)
# print(spec_char)

# for loop

# count = 0

# for w in word:
#     if w == char:
#        count += w.count(char)
# print(count)



''' Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

# user_name = input('Enter your name: ')
# user_age = int(input('Enter your age: '))

# hundred = 100 - user_age
# print(f"{user_name} will turn 100 in {hundred} years")

'''
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

'''

# first = int(input("Enter your 1st number: "))
# second = int(input("Enter your 2nd number: "))

# if (first * second) <= 1000:
#     print(first * second)
# else:
#     print(first + second)



'''
Write a program to accept a string from the user and display characters that are present at an even index number.
'''
str_input = input("Enter a word: ")
display_char = " "

for s in str_input[::2]: #[::2] allows to skip by 2
    display_char += s

# print(display_char)


'''
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
# test_string = "12345"
# start = 1

# for n in test_string:
#     print(n * start)
#     start += 1 # incremeting start by 1



''' 
Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
'''
# num_input = int(input("Enter a number: "))

# if num_input > 0:
#     print("Positive")
# elif num_input < 0:
#     print("Negative")
# else:
#     print("Zero")


'''
Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.
'''
# first method
# max_list = [int(input("Please enter a number: ")), int(input("Please enter a number: ")), int(input("Please enter a number: "))]
# print(f"The biggest number in the list is {max(max_list)}")


# second method
# first = int(input("Please enter a number: "))
# second = int(input("Please enter a number: "))
# third = int(input("Please enter a number: "))

# max_list = list()
# max_list.append(first)
# max_list.append(second)
# max_list.append(third)
# # print(max_list)

# result = max(max_list)
# print(result)

'''Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N taken from a user.'''

num_input = int(input("Please enter a number: "))
count = 0

while num_input.isnumerical():
     


'''
Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.
'''





'''
List Sum: Write a Python program to find the sum of all elements in a given list of integers.
my_list = [0, 2, 3, 4, 4, 5, 1, 9]
'''
my_list = [0, 2, 3, 4, 4, 5, 1, 9]


'''
List Average: Write a Python program to calculate the average of all elements in a given list of integers.
my_list = [0, 2, 3, 4, 4, 5, 1, 9]
'''

'''
List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.
my_list = [0, 2, 3, 4, 4, 5, 1, 9]
'''
# With a  for loop
# my_list = [0, 2, 3, 4, 4, 5, 1, 9]


# Max function


'''
List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.
'''
my_list = [0, 2, 3, 4, 4, 5, 1, 9]
squared_list = []
# For loop


# List comprehension

'''
Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.

The extend() method adds the specified list elements (or any iterable) to the end of the current list.
'''
# Lets see the extend method in action

# example from w3 schools
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# print(fruits)

my_super_list = [
    ['superman', 'wonderwoman','batman'],
    ['spiderman','captain america','ironman'],
    ['aquaman']
                 ]

# new_super = []

# for s in my_super_list:
#     new_super.extend(s)
# print(new_super)



'''
 Number Guessing Game: Write a Python program that generates a random number between 1 and 10 and lets the user guess the number. Use a `while` loop, `break` when the correct number is guessed, and `continue` to keep prompting the user until they guess correctly.
'''

# number_to_guess = random.randrange(0,10)

# print(number_to_guess)

# while True:
#     number_to_guess = random.randrange(0,10)
#     user_input = int(input("Please enter a number: "))
#     if user_input == number_to_guess:
#         print("Good Job, You guess the correct number")
#         break
#     else:
#         print("Number Incorrect. Guess again")
#         continue

# print()
