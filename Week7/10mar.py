class Person:
    def __init__(self,id,name):
        print("Object created! ")
        self.id = id
        self.name = name
class Student(Person):
    def __init__(self, id, name,sem,mark1,mark2):
        Person.__init__(self,id, name)
        self.sem = sem
        self.mark1 = mark1
        self.mark2 = mark2
    def avrmarks(self):
        total = self.mark1+self.mark2
        avg = total/2
        print("Average Marks: " ,avg)
        print()
    def getdata(self):
        print("Id: ",self.id)
        print("Name: ",self.name)
        print("Sem: ",self.sem)
        print("Marks1: ",self.mark1)
        print("Marks2: ",self.mark2)
    def __del__(self):
        print("Object Destroyed! ") 
"""
Problem: Vehicle Information System
Design a program using inheritance.
🔹 Base Class: Vehicle
Create a class Vehicle with the following attributes:
vehicle_id
brand
price

Methods:
display_vehicle()
Displays vehicle details.

🔹 Derived Class: Car (inherits from Vehicle)
Add the following additional attributes:
num_doors
fuel_type

Methods:
display_car_details()
Display all vehicle details along with car-specific information.

Tasks
Create at least 2 car objects.
Display their details.

"""

"""
Problem: Employee Salary Management System
Create a program using inheritance to manage employee salaries.

🔹 Base Class: Employee
Attributes
emp_id
name
base_salary

Methods:
display_employee(): Display employee details.
annual_salary(): Return yearly salary:
base_salary × 12

🔹 Derived Class: Manager
Additional attributes:
department
bonus

Methods:
total_salary(): Calculate total annual salary:
(base_salary × 12) + bonus
display_manager(): Display all manager details including department and total salary.

🔹 Tasks
Create multiple manager objects.
Store them in a list (array) of objects.
Display all managers' details.
"""
def main():
    """
    Problem  1: Student Information System
    x=Student(1,"Swayam",2,60,60)
    x.getdata()
    x.avrmarks()
    y = Student(2,"Swayam",1,80,90)
    y.getdata()
    y.avrmarks()
    """

if __name__ == "__main__":
    main()