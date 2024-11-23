import re
file = open("academic.txt",'r')
string = file.read()
pattern ="credit hours- (\\d+)\npoint - (\\d+.\\d+)"
data= re.findall(pattern,string)
print(data)
point=0
credit= 0
for i in data:
    point +=(int(i[0])*float(i[1]))
    credit += int(i[0])
print("CGPA : ",end=" ")
print(point/credit)
file.close()