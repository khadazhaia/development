# regex (may help to solve the patterns) use regex_completed file

# Print statement, Initialize any needed variables

print('''To sign up, enter a username and password.
      
The username must start with a lowercase letter, and only contain letters, numbers, and underscores.
      
The passowrd must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces.''')

username = " "
password = " "

taken_usernames = ["admin", "admin123", "superuser", "superuser123"]

error_messages = ["Username Taken", "Invalid Username", "Invalid Password"]

# Get username and password from user. Compare user entries with system username and password. Do they match? (Initialize loop to prompt user, give error messages)

while True:
    input("Please enter your username: ")
    input("Please enter your password: ")


# Incorrect username or password (Testing username, Testing password)

# Login Successful! (Handling successful login)