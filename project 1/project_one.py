# regex (help to solve the patterns)

import re

# Print statement, Initialize any needed variables

print('''To sign up, enter a username and password.
      
The username must start with a lowercase letter, and only contain letters, numbers, and underscores.
      
The passowrd must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces.\n''')

username, password = " ", " "

reprompt_username, reprompt_password = " ", " "

taken_username = ["admin", "admin123", "superuser", "superuser123"]

error_message = ["Username Taken", "Invalid Username", "Invalid Password", "Invalid Username or Password"]

special_character = ["!", "@", "#", "$", "%", "^", "&", "*"]

# Get username and password from user. Compare user entries with system username and password. Do they match? 
   # Initialize loop to prompt user, Not a taken username, Give error messages
while True:
   username = input("Please enter your username: ")
   username = username.strip()

   password = input("Please enter your password: ")
   password = password.strip()
  
   if username not in taken_username:
       pass
   else:
       print(error_message[0])
       continue
   
# Incorrect username or password  
   # Testing Username: starts with a lowercase letter and only contain letters, numbers and underscore 
   if username[0].islower() and username.isidentifier():
           print(f"Username: {username}")
   else:
       print(f"{error_message[1]}. Username must start with a lowercase letter and only contain letters, numbers and underscores")
       continue

   # Testing password: at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces
   if len(password) >= 8:
        print(f"{password} is at least 8 characters long")
   else:
        print(f"{error_message[2]} password must be at least 8 letters long")
        continue
   
   if  any(p.isupper() for p in password):
        print(f"{password} contain at least one uppercase letter")
   else:
        print(f"{error_message[2]} password must contain at least one uppercase letter")
        continue
    
   if any(p.islower() for p in password):
        print(f"{password} contain at least one lowercase letter")
   else:
        print(f"{error_message[2]} must contain at least one lowercase letter")
        continue
   
   if re.search(r'\d', password):
        print(f"{password} contain at least one digit")
   else:
        print(f"{error_message[2]} must contain at least one digit")
        continue
   if [p for p in password if p in special_character]:
        print(f"{password} contain at least one special charcater")
   else:
        print(f"{error_message[2]} must contain at least one special character")
        
        
#    if " " not in password[0:]:

# Login Successful! 
   # Handling Successful Login: Reprompt user
#    print("Congrats on signing up, please login ")
#    
#    re_prompt_username = input("Please enter your username: ")
#    re_prompt_username = re_prompt_username.strip()
#    
#    re_prompt_password = input("Please enter your password: ")
#    re_prompt_password = re_prompt_password.strip()
#    
#     if username == re_prompt_username and password == re_prompt_password:
#         print(f"Login Successful")
#         break
#     else:
#         print(error_message[3])
#         continue
 

