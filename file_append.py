# f=open("k.txt",'a')
# f.write("python")
# f.close()
from email.charset import add_codec

# s=open("l.txt",'r')
# content=s.read()
# s.close()
#
# f=open("k.txt",'a')
# f.write(content)
# f.close()

# f=open("k.txt",'a+')
# f.write("python")
# print(f.read())
# f.close()

# f=open("k.txt",'a+')
# print(f.tell())
# f.write("python")
# print(f.tell())
#
# f.seek(0)
# print(f.read())
# print(f.tell())
# f.close()

#to delete text file
# import os
# #os.remove(filename)
# os.remove("k.txt")
# print("File is deleted")
def add():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    sum=n1+n2
    print("Sum=",sum)

def sub():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    diff=n1-n2
    print("Difference=",diff)

def mul():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    mul=n1*n2
    print("Product=",mul)

def div():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    div=n1/n2
    print("Division=",div)

while(True):
    print("1.Add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")
    
    ch=int(input("Enter your choice:"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch ==4:
        div()
    else:exit()









































































