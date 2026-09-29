# # #write a program to read a text file and displays the number of lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print("Number of lines=",len(s))
# f.close()
# # #write a program to display the number of words in a file
# s=f.read()
# print(len(s.split()))
# f.close()
# # #write a program to update the second line in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s)
#
# s[1]="new line\n"
#
# f.close()
#
# f=open('k.txt','w')
# f.writelines(s)
# f.close()


# # #write a program to display the last 5 lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s[-5::])
#
# #program to search a particular word in a file
# f=open('k.txt','r')
# s=f.read()
# if "python" in s:
#     print(" word in file")
# else:
#     print("not in file")
# f.close()
# #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# s=f.read()
# count_l=0
# count_d=0
# count_s=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     elif i.isdigit():
#         count_d+=1
#     elif i.isspace():
#         count_s+=1
# print("letters=",count_l)
# print("digits=",count_d)
# print("spaces=",count_s)
# f.close()



#reverse the lines in a file
# f=open('k.txt','r')
# s=f.readlines()
# print(s)
#
# rev=s[::-1]
#
# f.close()
#
# f=open('k.txt','w')
# f.writelines(rev)
# f.close()

# A file totalstudents.txt.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line
f=open("totalstudents.txt",'r')
total=f.readlines()
f.close()

f=open("passedstudents.txt",'r')
passed=f.readlines()
f.close()

failed=[]

for i in total:
    if i not in passed:
        failed.append(i)

f=open("failedstudents.txt","w")
f.writelines(failed)
f.close()

print("Failed Students",failed)

