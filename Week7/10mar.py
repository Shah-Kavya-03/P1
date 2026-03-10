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

class Vehicle:
    def __init__(self,vehicle_id,brand,price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price
    def display_vehicle(self):
        print("Vehicle ID: ",self.vehicle_id)
        print("Brand: ",self.brand)
        print("Price: ",self.price)

class Car(Vehicle):
    def __init__(self,vehicle_id,brand,price,num_doors,fuel_type):
        Vehicle.__init__(self,vehicle_id,brand,price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    def display_car_details(self):
        self.display_vehicle()
        print("Number of Doors: ",self.num_doors)
        print("Fuel Type: ",self.fuel_type)

class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    def display_employee(self):
        print("Employee ID: ",self.emp_id)
        print("Name: ",self.name)
        print("Base Salary: ",self.base_salary)
    def annual_salary(self):
        return self.base_salary * 12

class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,department,bonus):
        Employee.__init__(self,emp_id,name,base_salary)
        self.department = department
        self.bonus = bonus
    def total_salary(self):
        return (self.base_salary * 12) + self.bonus
    def display_manager(self):
        self.display_employee()
        print("Department: ",self.department)
        print("Total Annual Salary: ",self.total_salary())

def main():
    #Problem  1: Student Information System
    x=Student(1,"Swayam",2,60,60)
    x.getdata()
    x.avrmarks()
    y = Student(2,"Swayam",1,80,90)
    y.getdata()
    y.avrmarks()

    #Problem 2: Vehicle Management System
    c1 = Car(101,"Toyota",20000,4,"Petrol")
    c1.display_car_details()
    print()
    c2 = Car(102,"Honda",25000,4,"Diesel")
    c2.display_car_details()
    print()

    #Problem 3: Employee Management System
    Employee_list = []
    m1 = Manager(1,"Alice",5000,"HR",10000)
    m2 = Manager(2,"Bob",6000,"IT",15000)
    Employee_list.append(m1)
    Employee_list.append(m2)
    m1.display_manager()
    print()
    m2.display_manager()

if __name__ == "__main__":
    main()