#Inheritance
# class Parent:
#     def m1(self):
#         print("In Parent Class Method m1")
#     def m2(self):
#         print("In Parent Class Method m2")
# # p=Parent()
# # p.m1()
# # p.m2()
# class Child(Parent):
#     def m1(self):
#         super().m1()
#         print("In child class m1")
#     def m3(self):
#         print("In Parent Class Method m3")
# c=Child()
# c.m3()
# c.m1()
# c.m2()


# class Person:
#     def __init__(self):
#         self.name=input("enter name:")
#         self.age=int(input("Enter age:"))
#     def show(self):
#         print(self.name,self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter rollno:"))
#         self.course=input("eEnter course:")
#         self.mark=int(input("Enter mark:"))
#     def show(self):
#         super().show()
#         print(self.rollno,self.course,self.mark)
#     def updatemark(self):
#         self.mark=print("enter new mark:")
#
# s=Student()
# s.updatemark()
# s.show()


# class Company:
#     def __init__(self):
#         self.company_name=input("Enter Company Name:")
#         self.location=input("Enter Location:")
#     def display_company(self):
#         print(self.company_name,self.location)
#
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter empid:"))
#         self.name=input("Enter name:")
#         self.designation=input("Enter Designation:")
#         self.salary=int(input("Enter Salary:"))
#     def display_details(self):
#         super().display_company()
#         print(self.empid,self.name,self.designation,self.salary)
#     def update_salary(self):
#         self.salary=1.1*self.salary
#         print("Updated Salary:",self.salary)
# e=Employee()
# e.display_details()
# e.update_salary()

# class Category:
#     def __init__(self):
#         self.category_name=input("Enter Category:")
#     def show_category(self):
#         print("Category Name:"self.category_name)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("Enter Product name:")
#         self.price=int(input("Enter Price:"))
#         self.quantity=int(input("Enter Quantity:"))
#     def total_price(self):
#         print("Total Price=",self.price*self.quantity)
# p=Product()
# p.total_price()
# p.show_category()

#Multiple Inheritance
class Hospital:
    def __init__(self):
        self.hos_name=input("Enter Hospital name:")
        self.location=input("Enter Location:")
        self.phone=int(input("Enter Phone number:"))
    def display_hospital(self):
        print(self.hos_name,self.location,self.phone)
class Department:
    def __init__(self):
        self.dept_name=input("Enter Department name:")
        self.doctor_name=input("Enter doctor name:")
    def display_department(self):
        print(self.dept_name,self.doctor_name)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("Enter Patient name:")
        self.age=int(input("Enter Age:"))
        self.gender=input("Enter Gender:")
        self.admission_date=input("Enter Admission Date:")
        self.bedno=int(input("Enter Bedno:"))
        self.discharge_date=""
    def set_discharge(self):
        self.discharge_date=input("Enter Discharge Date:")
    def full_summary(self):
        print("PATIENT SUMMARY")
        print("Hospital Details")
        Hospital.display_hospital(self)
        print("Department Details")
        Department.display_department(self)
        print("Patient Name:"self.patient_name)
        print("Age:"self.age)
        print("Gender:"self.gender)
        print("Admission Date:"self.admission_date)
        print("Bed Number:"self.bedno)
        print("Discharge Date:"self.discharge_date)
        if(self.discharge_date=="")
            print("Not Yet Discharge")
        else:
            print("Discharge Date:",self.discharge_date)

p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()