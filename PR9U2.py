file1= open("file1.txt","r")
file2= open("file3.txt","w")
data = file1.readline()
while(len(data)>0):
   s = data.split()
   print(s)
   for i in s:
     file2.write(i+" ")
   file2.write("\n")
   data=file1.readline()

file1.close()
file2.close()
