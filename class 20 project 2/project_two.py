
class Employee:

    def  __init__(self, name: str,job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self):
        return f"{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary}"

employee1 = Employee("Khadazhaia", "Python Developer", "Engineering", 125000, 2024)

print(employee1)
    