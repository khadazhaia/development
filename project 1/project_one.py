# regex (help to solve the patterns)

import re

# Print statement, Initialize any needed variables

print('''To sign up, enter a username and password.
      
The username must start with a lowercase letter, and only contain letters, numbers, and underscores.
      
The passowrd must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces.\n''')

user_name = " "
pass_word = " "

taken_usernames = ["admin", "admin123", "superuser", "superuser123"]

error_messages = ["Username Taken", "Invalid Username", "Invalid Password"]

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

# Get username and password from user. Compare user entries with system username and password. Do they match? (Initialize loop to prompt user, give error messages)

# Not a taken username
while True:
   username = input("Please enter your username: ")
   username = username.strip()
  
   if username not in taken_usernames:
       print(f"{username} is an available username")
   else:
       print(error_messages[0])
       continue
   
# Incorrect username or password (Testing username, Testing password)
   
   # starts wth a lowercase letter
   starts_lower_case =  username.startswith(username.lower())
   if starts_lower_case:
       print(f"{username} starts with a lowercase letter")
   else:
       print(f"{error_messages[1]}. Username must start with a lowercase letter")
       continue
        
   # may only contain letters, numbers and underscore (this code not working yet)
   if (username.isalnum() and "_" in username >= 0) or (username.isalpha and "_" in username >= 0):
            print(f"{username} is a valid username")   
   else:
       print(f"{error_messages[1]}. Username may only contain letters, numbers and underscores")
       continue


# if u.upper >= 1
# if u.lower >= 1
# if u.digit >= 1
# if u.count(_) >= 1
              
# Login Successful! (Handling successful login)