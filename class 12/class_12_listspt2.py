
import pandas as pd
import numpy as np
import statistics

''' Here's a neat trick '''

# This list contains 100, 1's.
list_1 = [1, 2, 3] * 25
# print(list_1)

''' Lists part 2, lists within lists  '''

# 2 dimensional list
two_dimensional_list = [["hello", "bye"], [1, 5]]

# access hello
# print(two_dimensional_list[0][0])

# access bye
# print(two_dimensional_list[0][1])

# access 1
# print(two_dimensional_list[1][0])

# access 5
# print(two_dimensional_list[1][1])


# Access all the elements in this list with bracket notation
my_list = ["hello", 1, ["dog", 3], "cat", [True, ["frog", 5]]]
#           [0]    [1]    [2]       [3]         [4]
# Access Hello
# print(my_list[0])

# Access 1
# print(my_list[1])

# Access Dog
# print(my_list[2][0])

# Access 3
# print(my_list[2][1])

# Access Cat
# print(my_list[3])

#Access True
# print(my_list[4][0])

#Access Frog
# print(my_list[4][1][0])

#Access 5
# print(my_list[4][1][1])

# Nested Loops
mdList = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# regular loop
# for n in mdList:
#      print(n)

# Access individual values in list with nested loops
# for n in mdList:  # Accesses the first dimension
#     for val in n:  # Accesses the second dimension
#         print(val)


''' Exercise
Write a 2D list that is a 3x3 grid of numbers.
Write some code that prints out that grid nicely with proper formatting.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 2 3
4 5 6
7 8 9

'''

lis = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# for r in lis:
#     print(*r)
# Loop through to access 2nd dimension integers
# for rows in lis: # access our first dimension
#     for columns in rows: # access our second dimension
#        # Format as directed
#        print(columns, end=' ') # will add the space between our integers
#     print() # add a carriage return


'''
Write some code that goes through a 2D list and prints the columns.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 4 7
2 5 8
3 6 9
Hint: First create a new 2D list with swapped rows and columns. (You will need 2 nested for loops.) Then it's the same as the last problem.
'''

lis = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lis_2 = []

# For loop transposes
# for i in range(len(lis[0])):
#     row = [] # temporary holding place for our integers
#     for item in lis:
#         row.append(item[i])
#     lis_2.append(row) # this will capture the swapped data
# print(lis_2)

# Unpacking with star operator
# for l in lis_2:
#     print(*l)
# For loop formats transposing
# for rows in lis_2:
#     for columns in rows:
#         print(columns, end=' ')
#     print()

# With Pandas
# df = pd.DataFrame(lis)
# transposed_list = pd.DataFrame(df).transpose().values.tolist() #transposing than converting to a list
# print(transposed_list)
# print in for loop for print's carriage return 
# for i in transposed_list:
#     for rows in i:
#         print(rows, end=' ')
#     print()

# With numpy
# transposed_list = np.transpose(lis)
# print(transposed_list)

'''
You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
For example, if this is your list:
data = [[45,56,89],[67,34,78],[23,67,34]]
This would be your output:
Column 1: Sum = 135, Average = 45.0
Column 2: Sum = 157, Average = 52.33
Column 3: Sum = 201, Average = 67.0
Hint: Make a list to store the sums, and a list to store the averages.


'''

data = [[45,56,89],[67,34,78],[23,67,34]]

# data_columns = []

# Transpose data
# for i in range(len(data[0])):
#     temp_list = [] # temporary holding place for our integers
#     for my_columns in data:
#         temp_list.append(my_columns[i])
#     data_columns.append(temp_list) # this will capture the swapped data
# print(data_columns)
# transposed_data = np.transpose(data)

# Using Numpy
# data_columns = np.transpose(data)
# print(data_columns)

# Format for output
# print(f'''
# Column 1: Sum = {sum(data_columns[0])}, Average = {statistics.mean(data_columns[0])} 
# Column 2: Sum = {sum(data_columns[1])}, Average = {statistics.mean(data_columns[1]) :.2f}
# Column 3: Sum = {sum(data_columns[2])}, Average = {statistics.mean(data_columns[2])}
# ''')
# List Comprehension

# For Loop
# Add veggies less than 6 letters to new list
vegetables = ['broccoli', 'kale', 'onion', 'garlic']

# short_vegetables = []
# for v in vegetables:
#     if len(v) < 6: # if vegetable is less than 6 charcacters
#         short_vegetables.append(v) # appeend ro short vegetable
# print(short_vegetables)

# List comprehension
# vegetables = ['broccoli', 'kale', 'onion', 'garlic']

# short_vegetables = [v for v in vegetables if len(v) < 6]
# print(short_vegetables)

''' Exercise
You are given a list of integers. Write a Python program to create a new list that only includes the even numbers from the original list.
You can do this in one line with a list comprehension.
Example:
original_list = [34, 57, 81, 92, 2, 13]
new_list = [34, 92, 2]
'''

''' List comprehension for conditions'''
# With a For Loop
original_list = [34, 57, 81, 92, 2, 13]
new_list = []

# for l in original_list:
#     if l % 2 == 0:
#         new_list.append(l)
# print(new_list)

# With list comprehension
# original_list = [34, 57, 81, 92, 2, 13]
# new_list = [l for l in original_list if l % 2 == 0]
# print(new_list)

''' List comprehension with expressions'''

# Lets add 5 to every item in this list
# numbers = [0, 2, 3, 8, 9, 11, 20]
# plus_five = [n + 5 for n in numbers]
# print(plus_five)


# We can add two lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]

third_list = [x for x in first_list] + [x for x in second_list]
# print(third_list)

# Multiply items from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

product_list = [list1[i] * list2[i] for i in range(len(list1))]
# print(product_list)

'''
Exercise

You work for a sales company and must generate a list of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a list of customers over 60, and a list of customers who have made at least 5 purchases. Use a list comprehension to output a list of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']
Output: ['Dominic', 'Simone']

'''

over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']

customer_discount = []

# For Loop
for c in over_60_years:
    if c in over_5_purchases:
        customer_discount.append(c)
print(customer_discount)

# List comprehension

customer_discount = [c for c in over_60_years if c in over_5_purchases]
print(customer_discount)