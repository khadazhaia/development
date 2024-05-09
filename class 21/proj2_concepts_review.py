from datetime import datetime

'''Write a program that will take the user's first name, and than the users last name, and print the value to a text file on 2 separate lines'''

# one method
# firstname = input("First name: ")
# lastname = input("Last name: ")

# f = open("my_output.txt", "w") # we are opening a new file
# f.write(f"{firstname}\n{lastname}")
# f.close()

# with open (preferred method)
# with open("fullname.txt", "w") as output:
#     firstname = input("First name: ")
#     lastname = input("Last name: ")
#     output.write(f"{firstname}\n{lastname}")

''' Write a function called find_even_numbers that will take in a list of integer values and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''

# def find_even_number(my_list):

#     output_list = []
#     for m in my_list:
#        if m % 2 == 0:
#            output_list.append(m)

#     with open("even_nums.txt", "w") as output:
#         for o in output_list:
#             o = str(o)
#             output.writelines(o)

#     print("File Printed Successfully")
           
# my_list = [1,2,3,4,5,6,7,12,14,15,21,22] # this is the data we pass into our function

# find_even_number(my_list) # this is our function call

''' Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''

# with open("time_to_say_goodbye.txt", "r") as lyrics:
    # my_paragraph = lyrics.read() # will read in everything
    # my_line = lyrics.readline() # one line at a time
    # lyric_list = lyrics.readlines() # will deliver a list

# print(my_paragraph) 
# print(my_line)
# print(lyric_list)




''' Bank account class 
Create the bank account class per the specifications in the powerpoint.  

1. Test string 
'''
class BankAccount:
     # Constructor
     def __init__(self, customer_name:str, acct_num:int, date: str, balance: float):
          self.customer_name = customer_name
          self.acct_num = acct_num
          self.date = date
          self.balance = balance
     # String representation
     def __str__(self):
          return f'''Customer name: {self.customer_name}\nAccount number: {self.acct_num}\nDate of opening: {self.date}\nBalance: ${self.balance:.02f}'''
     # Make a deposit, update the amount
     def deposit(self, amount):
          self.balance += amount
          print(f'{amount} has been deposited in your account')

     # Make a withdrawal, update the amount
     def withdraw(self, amount):
          if amount > self.balance:
            print("Sorry, insufficient funds")
          else:
            self.balance -= amount
            print(f'{amount} has been withdrawn from your account')

     def check_balance(self):
         print(f"Your current balance is {self.balance}")

     def days_since_opened(self):
         open_date =datetime.strptime(self.date, "%m-%d-%y")
         today = datetime.now()
         days_since_opened = today - open_date
         return f"Account opened: {days_since_opened.days} days ago"
    
     def print_customer_details(self):
         f = open("customer_details.txt", "w")
         f.write(f'''Customer name: {self.customer_name}\nAccount number: {self.acct_num}\nDate of opening: {self.date}\nBalance: ${self.balance:.02f}\n{self.days_since_opened()}''')
         f.close()

ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000.25 )
ac_no_2 = BankAccount("Jim Jones", 5424, "01-05-22", 1000 )
ac_no_3 = BankAccount("Sally Field", 3242, "11-04-15", 1000 )
ac_no_4 = BankAccount("Burt Reynolds", 4325, "08-11-13", 1000 )

# String representation - what happens when i print?
# print(ac_no_1)

# ac_no_1.check_balance()
# ac_no_1.deposit(500)

# ac_no_1.check_balance()
# ac_no_1.withdraw(250)

# ac_no_1.check_balance()

# print(ac_no_1.days_since_opened())

ac_no_1.print_customer_details()