
class Student:
    def __init__(self,rollno,name,mark):
        self.rollno=rollno
        self.name=name
        self.marks=marks
students=[]
while(True):
    print("1.Add Student")
    print("2.Update Marks")
    print("3.Display All Student Details")
    print("4.Search Student by Roll Number")
    print("5.Delete Student")
    print("6.Exit")

    ch=int(input("Enter your choice:"))

    if(ch==1):
        rollno=int(input("Enter Rollno:"))
        name=input("Enter Name:")
        marks=int(input("Enter marks:"))
        s=Student(rollno,name,marks)
        students.append(s)
        print("Student added successfully")
    elif(ch==2):
        rollno=int(input("Enter Rollno:"))
        for s in students:
            if(s.rollno==rollno):
                s.marks=int(input("Enter new marks:"))
                print("Marks updated successfully")
                break
        else:
            print("Student does not exist")
    elif(ch==3):
        for s in students:
            print("Rollno:",s.rollno)
            print("Name:",s.name)
            print("Marks:",s.marks)

    elif(ch==4):
        rollno=int(input("Enter Rollno:"))
        for s in students:
            if (s.rollno == rollno):
                print("Rollno:",s.rollno)
                print("Name:", s.name)
                print("Marks:", s.marks)
                break

        else:
            print("Student not found")
    elif(ch==5):
        rollno = int(input("Enter Rollno:"))
        for s in students:
            if (s.rollno == rollno):
                students.remove(s)
                print("Student Deleted")
                break
        else:
            print("Student not found")

    else:
        exit()

