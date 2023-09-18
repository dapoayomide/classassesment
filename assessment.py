'''
Define a class called Employee with a constructor that takes a name and a salary.
# The class should have a method called get salary that returns the salary of the employee.
# Define two subclasses of Employee called Manager and Engineer, that inherit from Emplovee
and have their own bonus attribute.
# The Manager class should have a bonus of 10% of the salary and the Engineer class should
have a bonus of 5% of the salary.
# The subclasses should override the get salary method to return the salary plus the bonus.
# Write a function called payroll that takes a list of employees and prints their name and salary.
# Create a list of employees with different names and salaries and pass it to the payroll function.
'''

class Employee:
     def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
     def get_salary(self):
         return self.salary

class Manager(Employee):

    def salary_bonus(self):
        return int(self.salary * 2)

class Engineer(Employee):

    def salary_bonus2(self):
        return int(self.salary * 2)
    



manager = Manager('dapo',100000)
engineer = Engineer('Teni',200000)

print(manager.salary_bonus())
print(engineer.salary_bonus2())
