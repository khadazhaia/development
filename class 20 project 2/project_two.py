'''
The system allows the business to store and manage employee data, and perform tasks related to employee management, such as adding and removing employees, updating employee information, searching for employees by name or department, and calculating total salary expenses.
'''

'''Methods
__str__(): return a string representation.
years_worked(): return the total years this employee has worked here, based on the hire year.
total_expense(): calculate the total salary expense for this employee, which is the salary multiplied by the years worked.
write_employees(): Write your employee information to a text file.
Add accessor and mutator methods for each attribute so a user doesn't need to access them directly. 
Be sure to use type hinting and a docstring in your class'''

class Employee:

    def  __init__(self, name: str,job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self):
        return f"{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary}"

employee1 = Employee("Zhaia", "Software Engineer", "Engineering", 125000, 2020)
employee2 = Employee("Ally", "Software Engineer", "Engineering", 130000, 2020)
employee3 = Employee("Nas", "Data Scientist", "Data", 125000, 2023)
employee4 = Employee("Tye", "Accountant", "Finance",90000, 2021)
employee5 = Employee("Zena", "Executive Assistant", "Operations", 90000, 2022)
employee6 = Employee("Des","Human Resources Manager", "HR", 80000, 2021)



print(employee1)
    