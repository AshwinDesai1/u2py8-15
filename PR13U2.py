import re
def printRecord(i):
    print(i)
def nonStudent(l):
    pattern = "faculty$"
    for i in l:
        if(re.search(pattern,i)):
            printRecord(i)
            
def iit(l):
    for i in l:
        i=i.lower()
        if(i.find("iit")!=-1):
            printRecord(i)
def findDuplicate(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if(i!=j and (l[i])==(l[j])):
                print("Record : ",i," and ",j," is duplicate")
                print(l[i])
                print(l[j])
def groupByAffiliation(l):
    pattern = "(\d{10}),(.+)(student|faculty)"
    affiliation=[]
    for i in range(0,len(l)):
         affiliation.append(re.findall(pattern,l[i],re.DOTALL)[0][1])
       
    for i in range(0,len(affiliation)):
        for j in range(i,len(affiliation)):
            if affiliation[i]>affiliation[j]:
                temp=affiliation[j]
                affiliation[j]=affiliation[i]
                affiliation[i]=temp
                temp=l[j]
                l[j]=l[i]
                l[i]=temp   
    for i in l:
        print(i)

fh = open("conference_data.txt","r")
fh.readline()          
t = fh.read()

l=[]
participate1="student"
participate2="faculty"
start=0

while(start<len(t)):
    s=t.find(participate1,start)
    f=t.find(participate2,start)
    
    if((s<f or f==-1)and s!=-1):
        l.append(t[start:s+7])
        start=s+7+1
    else:
        l.append(t[start:f+7])
        start=f+7+1
    print(start,len(t))
print("\n---------------------------")
print("Non Student data is follow\n")
nonStudent(l)
print("\n---------------------------")
print("iit affiliation data is follow\n")
iit(l)
print("\n---------------------------")
print("duplicate data is follow\n")
findDuplicate(l)
print("\n---------------------------")
print("group of affiliation is follow\n")
groupByAffiliation(l)
        