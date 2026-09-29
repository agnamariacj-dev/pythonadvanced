# class Circle:
#     def __init__(self):
#         self.radius=input("Enter radius:")
#     def getarea(self):
#         print("Area=",3.14*int(self.radius)*int(self.radius))
#     def getperimeter(self):
#         print("Perimeter=",2*3.14*int(self.radius))
# c=Circle()
# c.getarea()
# c.getperimeter()


class Account:
    def __init__(self):
        print("Account Details")
        self.acctnumber=int(input("Enter Account number:"))
        self.acctname=input("Enter account name:")
        self.balance=int(input("Enter balance:"))

    def showbalance(self):
        print("Current Balance=",self.balance)
    def deposit(self):
        amount=int(input("Enter the deposit amount:"))
        self.balance=amount+self.balance
        self.showbalance()
    def withdraw(self):
        amount=int(input("Enter amount to withdraw:"))
        if(amount>self.balance):
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            self.showbalance()
a=Account()
a.showbalance()
a.deposit()
a.withdraw()

# l=[]
# while(1):
#     print("Bank Operations")
#     print("1.Create Account")
#     print("2.Withdraw")
#     print("3.Deposit")
#     print("4.Showbalance")
#     print("5.exit")
#
#     ch=int(input("Enter your choice:"))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#     elif ch==2:
#         number=int(input("Enter account number:"))
#         for i in l:
#             if(i.acctnumber==number):
#                 i.withdraw()
#                 break
#         else:
#             print("Account does not exist")
#     elif ch==3:
#         number = int(input("Enter account number:"))
#         for i in l:
#             if(i.acctnumber==number):
#                 i.deposit()
#                 break
#         else:
#             print("Account does not exist")
#
#
#     elif ch==4:
#         number = int(input("Enter account number:"))
#         for i in l:
#             if (i.acctnumber == number):
#                 i.showbalance()
#                 break
#         else:
#             print("Account does not exist")
#     else:
#         exit()
#     a1=Account()
#     a2=Account()


# l=[a1,a2]
# for i in l:
#     # print(i.acctname,i.acctnumber,i.balance)
#     # i.showbalance()
#     if(i.acctnumber==123):
#         i.showbalance()



























































