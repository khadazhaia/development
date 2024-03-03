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

email = input("Hello, please enter your email address: ")

# Sanitize Data
email = email.strip()

# Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == ".")
print(f"Test 1: Does the email have '.' at the third-to-last index? {test_1}\n")

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = (email.count("@") == 1) and (email[-5] > "@")
print(f"Test 2: Does the email have exactly one '@' symbol, at the fifth-to-last index or earlier? {test_2}\n")

# Test 3: There is at least one character before the "@" symbol
test_3 = (email[0] > "@")
print(f"Test 3: Does the email have atleast one character before the '@' symbol? {test_3}\n")

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = (" " not in email[0:])
print(f"Test 4: Does the email not have any spaces? {test_4}\n")

#Final Test with and Keyword

final_test = test_1 and test_2 and test_3 and test_4
print(f"Final Test: Are all the above tests True? {final_test}")
