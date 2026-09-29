# #sum
# try:
#     num1=int(input("Enter num1:"))
#     num2=int(input("Enter num2:"))
#     s=num1+num2
# except:
#     print("Invalid number")
# #optional
# else:
#     print("Sum",s)
# finally:
#     print("done")

# #division
# try:
#     num1=int(input("Enter num1:"))
#     num2=int(input("Enter num2:"))
#     r=num1/num2
#     print("Result",R)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except ValueError:
#     print("Value Error")
# except:
#     print("Error")

#1.
# import math
# while(True):
#     try:
#         n=int(input("Enter number:"))
#         r=math.factorial(n)
#         print("Factorial:",r)
#         break
#     except:
#         print("Invalid Input")

#2.
# while(True):
#     try:
#
#         print("1.Addition")
#         print("2.Subtraction")
#         print("3.Multiplication")
#         print('4.Division')
#         print('5.Exit')
#         ch=int(input("Enter your choice:"))
#         if ch in [1,2,3,4]:
#             n = int(input("Enter number:"))
#             m = int(input("Enter a number:"))
#             s=n+m
#             d=n-m
#             p=n*m
#             q=n/m
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Value Error")
#     except:
#         print("Error")
#     else:
#         if ch==1:
#             print("Result",s)
#         elif ch==2:
#             print("Result",d)
#         elif ch==3:
#             print("Result",p)
#         elif ch==4:
#             print("Result",q)
#         else:
#             exit()


# try:
#     f=open("k.txt",'r')
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File does not exist")


# d={"name":"arun","age":34,"place":"ekm"}
# try:
#     key=input("Enter key:")
#     print("Value:",d[key])
# except KeyError:
#     print("Key does not exist")