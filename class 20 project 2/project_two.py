from datetime import datetime
import datetime

'''
The system allows the business to store and manage employee data, and perform tasks related to employee management, such as adding and removing employees, updating employee information, searching for employees by name or department, and calculating total salary expenses.

1.
2.
3.
4.
'''

# creating employee class
class Employee:
    
     # intitalization, attributes, type hinting, docstring
     def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
         self.name = name
         self.job_title = job_title
         self.department = department
         self.salary = salary
         self.hire_year = hire_year

     # __str__(): return a string representation
     def __str__(self):
         return f"{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary:.02f}"
    
     # years_worked(): return the total years this employee has worked here, based on the hire year
     def years_worked(self):
         today = datetime.datetime.now()
         year = today.year
         return year - self.hire_year
    
     # total_expense(): calculate the total salary expense for this employee, which is the salary multiplied by the years worked  
     def total_expense(self):
         return self.salary * self.years_worked()
  
     # write_employees(): Write employee information to a text file
     def write_employees(self):
         f = open("employee_information.txt", "w")
         f.write(f'''{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary:.02f}''')
         f.close()
    
     # add accessor and mutator methods for each attribute so a user doesn't need to access them directly
     
     # Mutator method for name
     def set_name(self, new_name):
        self.name = new_name

     # Mutator method for job_title
     def set_job_title(self, new_job_title):
        self.job_title = new_job_title

     # Mutator method for department
     def set_department(self, new_department):
        self.department = new_department
    
     # Accessor method
     # Accessor method for name (outputs name)
     def get_name(self):
        return self.name
    
     # Accessor method for job_title (outputs job_title)
     def get_job_title(self):
        return self.job_title
     
     # Accessor method for department (outputs department)
     def get_department(self):
        return self.department
     

employee1 = Employee("Zhaia", "Software Engineer", "Engineering", 125000, 2020)
employee2 = Employee("Ally", "Software Engineer", "Engineering", 130000, 2020)
employee3 = Employee("Nas", "Data Scientist", "Data", 125000, 2023)
employee4 = Employee("Tye", "Controller", "Finance",100000, 2021)
employee5 = Employee("Zena", "Executive Assistant", "Operations", 90000, 2022)
employee6 = Employee("Des", "HR Manager", "HR", 85000, 2021)
    
# testing
# print(employee1)

# print(employee1.years_worked())
    
# print(employee1.total_expense())

# employee1.write_employees()

print(employee1.set_name("Amy"))