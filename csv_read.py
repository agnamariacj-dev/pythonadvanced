#read
import csv
f=open("data.csv",'r')
r=csv.reader(f)
for i in r:
    print(i)
    # print(i[0])
    # print(i[1])
   # print(i[2])
f.close()