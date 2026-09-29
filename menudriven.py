# def add():
#     n1 = int(input("Enter n1:"))
#     n2 = int(input("Enter n2:"))
#     sum = n1 + n2
#     print("Sum=", sum)
#
#
# def sub():
#     n1 = int(input("Enter n1:"))
#     n2 = int(input("Enter n2:"))
#     diff = n1 - n2
#     print("Difference=", diff)
#
#
# def mul():
#     n1 = int(input("Enter n1:"))
#     n2 = int(input("Enter n2:"))
#     mul = n1 * n2
#     print("Product=", mul)
#
#
# def div():
#     n1 = int(input("Enter n1:"))
#     n2 = int(input("Enter n2:"))
#     div = n1 / n2
#     print("Division=", div)
#
#
# while (True):
#     print("1.Add")
#     print("2.sub")
#     print("3.mul")
#     print("4.div")
#     print("5.exit")
#
#     ch = int(input("Enter your choice:"))
#     if ch == 1:
#         add()
#     elif ch == 2:
#         sub()
#     elif ch == 3:
#         mul()
#     elif ch == 4:
#         div()
#     else:
#         exit()

# def file_read():
#     filename=input("Enter the filename")
#     f=open(filename,'r')
#     content=f.read()
#     print(content)
#     f.close()
#
# def file_write():
#     filename=input("Enter the filename")
#     f=open(filename,'w')
#     content=input("Enter the content")
#     f.write(content)
#     f.close()
#
# def file_append():
#     filename = input("Enter the filename")
#     f = open(filename, 'a')
#     content = input("Enter the content")
#     f.write(content)
#     f.close()
#
# def file_search():
#     filename = input("Enter the filename")
#     word=input("Enter the word to search:")
#     f=open(filename,'r')
#     content=f.read()
#
#     if word in content:
#         print("Word found")
#     else:
#         print("Word not found")
#     f.close()
#
# def file_delete():
#     import os
#     filename=input("Enter the filename:")
#     os.remove(filename)
#     print("File deleted")
#
# while(True):
#     print("1.File Read")
#     print("2.File Write")
#     print("3.File Append")
#     print("4.File Search")
#     print("5.File Delete")
#     print("6.Exit")
#
#     ch=int(input("Enter your choice:"))
#
#     if ch==1:
#         file_read()
#     elif ch==2:
#         file_write()
#     elif ch==3:
#         file_append()
#     elif ch==4:
#         file_search()
#     elif ch==5:
#         file_delete()
#     elif ch==6:
#         exit()




