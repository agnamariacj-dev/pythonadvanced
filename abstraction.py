# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter Length:"))
#         self.breadth=int(input("Enter breadth:"))
#     def get_area(self):
#         print("Area=",self.length*self.breadth)
#     def get_perimeter(self):
#         print("Perimeter=",2*(self.length*self.breadth))
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("Enter side:"))
#
#
#     def get_area(self):
#             print("Area=",self.side * self.side)
#
#     def get_perimeter(self):
#             print("Perimeter=",4*self.side)
# s=Square()
# s.get_area()
# s.get_perimeter()

from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self):
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.empid=int(input("Enter Empid:"))
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input("Enter Monthly Salary:"))
    def calculate_salary(self):
        print("Salary=",self.monthly_salary)
class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hours=int(input("Enter working hours:"))
        self.rate=int(input("Enter rate:"))
    def calculate_salary(self):
        print("Salary=",self.hours*self.rate)
f=FullTimeEmployee()
f.calculate_salary()
p=PartTimeEmployee()
p.calculate_salary()
