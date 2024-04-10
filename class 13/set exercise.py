'''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''

# instructions
print('''\nPython and JS Developer Tracker
Instructions
Input 's' or 'stop' at anytime to exit program
To add a Python developer type 'p' when prompted.
To add a JavaScript developer type 'js' when prompted.\n''')

# intialize our variables
developer_tracker, developer_name = "", ""
both_languages = set()
javascript_only = set()
python_only = set()
either_languages = set()


# put our error messages in a tuple
error_messages = ("Thank you, have a nice day", "no data")

# while loops
while True:

# inputs
    developer_tracker = input("Type 'P' for Python developer, 'JS' for JavaScript developer, or 'STOP' to exit program: ")

# string methods for cleanup if needed .strip(), .upper()
    developer_tracker = developer_tracker.strip().upper()    

# if statements, break keyword, pass 
    if developer_tracker != "STOP": 
         pass
    else:
         break

#inputs  
    developer_name = input("Enter developer name: ")

# string methods for cleanup if needed .strip(), .title()
    developer_name = developer_name.strip().title()

# if statements, break keyword, pass 
    if  developer_name != "Stop":
        pass
    else:
        break
  
# if statements
    
    if developer_tracker == "JS":
       javascript_only.add(developer_name)
    if developer_tracker == "P":
       python_only.add(developer_name)

# sets
    both_languages = javascript_only.intersection(python_only)
    either_languages = javascript_only.symmetric_difference(python_only)
    javascript_only = javascript_only.difference(python_only)

# print statement, formatted strings
    print("RESULTS:\n")
    print(f"The following developers know both languages: {both_languages}")
    print(f"The following developers know JavaScript but not PYTHON: {javascript_only}")
    print(f"The set of employees that know Python or JavaScript, but not both: {either_languages}")
    
print(error_messages[0])












