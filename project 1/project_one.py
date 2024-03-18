# regex (may help to solve the patterns) use regex_completed file

# Print statement, Initialize any needed variables

print('''To sign up, enter a username and password.
      
The username must start with a lowercase letter, and only contain letters, numbers, and underscores.
      
The passowrd must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces.\n''')

username = " "
password = " "

taken_usernames = ["admin", "admin123", "superuser", "superuser123"]

error_messages = ["Username Taken", "Invalid Username", "Invalid Password"]

lower_case = ["a", "b", "c", "d", "e", "f", "g", "h"]

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

numbers = list(range(10))


# Get username and password from user. Compare user entries with system username and password. Do they match? (Initialize loop to prompt user, give error messages)

while True:
   user_input = input("Please enter your username: ")
   user_input = user_input.strip()
   print(user_input)
   continue
   for u in user_input:
          if u in taken_usernames:
            print(error_messages[0])
            continue
          elif u not in taken_usernames and len(u) >= 8:
            print("The length is greater than 8")
        
          
# if u.upper >= 1
# if u.lower >= 1
# if u.digit >= 1
# if u.count(_) >= 1
# user_input = " " # initialization
# pet_name = [] # This will capture animal names

# while user_input != "stop":
#     user_input = input("Please enter your pets name: ")
#     if user_input == "stop": # This is to not add stop to the list
#         break
#     elif user_input not in pet_name:
#         pet_name.append(user_input)
#     else:
#         print(f"{user_input} is already in the list")

# print(pet_name)

        


# Incorrect username or password (Testing username, Testing password)

# Login Successful! (Handling successful login)