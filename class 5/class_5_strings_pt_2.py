''' Strings Part 2'''

# Strings are immutable

str_1 = 'BLUE' 
str_1.lower()
#print(str_1) # .lower string method has not changed string

str_2 = str_1.lower()
# print(str_2)  # new string with lower method

day = '  TUESDAY   ' # Create a new string with no whitespace 
day_1 = day.strip()
# print(day_1)
# print(len(day))
# print(len(day_1))

'''Indexing, with square brackets'''

word = 'Jasmine'

first_letter = word[0]
# print(first_letter)

# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])
# print(word[6])
# print(word[7]) # Lets note the error

# Create a variable to capture the first letter of this string
greeting = 'hello'
first_position = greeting[0]
# print(first_position)

last_position = greeting[len(greeting)-1] # Grabbing the length minus 1 and applying to the string will get the last position
# last_position = greeting[-1]
# print(last_position)

# Using the length and bracket notation, access the last letter in the variable below
month = 'February'
last_letter = month[len(month)-1]
# print(last_letter)

# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'
letter_x = first_name[3]
# print(letter_x)

letter_e = first_name[2]
# print(letter_e)

letter_d = first_name[6]
# print(letter_d)

'''Reverse indexing'''
fav_animal = 'Ostrich'

# print(fav_animal[-1])
# print(fav_animal[-2])
# print(fav_animal[-3])
# print(fav_animal[-4])
# print(fav_animal[-5])
# print(fav_animal[-6])
# print(fav_animal[-7])
# print(fav_animal[-8]) # Lets note the error

# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p
fav_season = 'spring'

letter_g = fav_season[-1]
# print(letter_g)

letter_i = fav_season[-3]
# print(letter_i)

letter_p = fav_season[-5]
# print(letter_p)

''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'
slice_of_fav_food = fav_food[2:6] # [start:stop] exclude the character at stop
# print(slice_of_fav_food)

# Using slicing please create a string that accesses 'rica' in 'America'

country = 'America'
slice_of_country = country[3:7]
# print(slice_of_country)

# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'
cartoon = 'Dora the explorer'
slice_of_cartoon = cartoon[1:4]
# print(slice_of_cartoon)

# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'
cartoon = "Dora the explorer"
slice_of_cartoon = cartoon[9:14]
# print(slice_of_cartoon)

# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'
slice_of_boxer = boxer[7:11]
# print(slice_of_boxer)

# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'
# print(superheroine[2:len(superheroine):2])

# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'
# print(word[0:len(word):4])

'''Slicing in reverse '''

random_word = 'daycare' # Excludes the start character
# print(random_word[::-1]) # Full daycare in reverse
# print(random_word[5:0:-1]) # aycar
# print(random_word[6:0:-1]) # eracya


'''
Write some code to print the second half of a string.


Example:
python
hon

'''
# Create a variable for word
language = "python"

# Create a varibale to get half of the length of the word
half = int(len(language) / 2)
# print(type(half))

# Create final bracket notation
result = language[half:len(language)]
# print(result)

#shorten version of the code above
language = "python"
# print(language[int(len(language) / 2):len(language)])

'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
# 
# email = input("Hello, please enter your email address: ")

# Sanitize Data
# email = email.strip()

# Test 1: It has a "." at the third-to-last index
# test_1 = (email[-4] == ".")
# print(f"Test 1: Does the email have '.' at the third-to-last index? {test_1}\n")

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
# test_2 = (email.count("@") == 1) and (email[-5] > "@")
# print(f"Test 2: Does the email have exactly one '@' symbol, at the fifth-to-last index or earlier? {test_2}\n")

# Test 3: There is at least one character before the "@" symbol
# test_3 = (email[0] > "@")
# print(f"Test 3: Does the email have atleast one character before the '@' symbol? {test_3}\n")

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
# test_4 = (" " not in email[0:])
# print(f"Test 4: Does the email not have any spaces? {test_4}\n")

#Final Test with and Keyword

# final_test = test_1 and test_2 and test_3 and test_4
# print(f"Final Test: Are all the above tests True? {final_test}")


# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''
# userin = input("Please enter your input: ")
# print("You entered", userin, sep=": ", end=".")

# round a float

long_num = 12.34567890
long_num = round(long_num, 2)
# print(long_num)

'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342
price = round(price, 2)

# print(f"""Dear {name},
# Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
# We appreciate your business and look forward to serving you again.
# Sincerely,
# The ABC Company""")

'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''

user_input = input("Please enter a word: ")

word = user_input[0:] == user_input[::-1]

print(f"Is the word a palindrome (same forwards and backwords)? {user_input}: {word}")