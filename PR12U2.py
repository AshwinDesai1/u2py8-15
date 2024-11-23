def add(name,phone,github):
    fh=open("file5.txt",'a+')
    fh.write("\nName : "+name+"\nPhone : "+phone+"\nGithub : "+github)
    fh.flush()
    fh.close()
    return True
def remove(name,phone,github):
    fh1=open("file5.txt","r")
    content=fh1.read()
    fh1.close()
    f="Name : "+name+"\nPhone : "+phone+"\nGithub : "+github
    index=content.find(f)
    endind=index+len(f)-1
    if index !=-1:
       newc=content[:index]+content[endind+1:]
       print(len(newc))
       print(newc)
       fh=open("file5.txt","w")
       fh.seek(0)
       fh.write(newc)
       fh.flush()
       fh.close()
       return True
    else:
        return False

def updatePhone(name,phone):
    fh=open("file5.txt","r")
    content=fh.readlines()
    fh.close()
    f="Name : "+name+"\n"
    c=0
    for i in range(len(content)):
        if f == content[i]:
            c+=1
            newp=content[i+1][:8]+phone+"\n"
            content[i+1]=newp
    if c!=0:
        fh=open("file5.txt","w")
        fh.writelines(content)
        fh.flush()
        fh.close()
        return True
    else:
        return False

def updateGithub(name,github):
    fh=open("file5.txt","r")
    content=fh.readlines()
    fh.close()
    f="Name : "+name+"\n"
    c=0
    for i in range(len(content)):
        if f == content[i]:
            c+=1
            newg=content[i+2][:9]+github+"\n"
            content[i+2]=newg
    if c!=0:
        fh=open("file5.txt","w")
        fh.writelines(content)
        fh.flush()
        fh.close()
        return True
    else:
        return False
      
def printByName(name):
    fh=open("file5.txt","r")
    content=fh.readlines()
    fh.close()
    f="Name : "+name+"\n"
    c=0
    l=list()
    for i in range(len(content)):
        if f == content[i]:
            c+=1
            for j in range(3):
                l.append(content[i+j])
    if f!=0:
        return l
    else:
        return 0

def printAll():
    fh=open("file5.txt","r")
    content = fh.read()
    fh.close()
    return content

def readAll():
    fh=open("file5.txt","r")
    content = fh.read()
    fh.close()
    return content
    

while True:
    print("1 for add ")
    print("2 for remove ")
    print("3 for update phone no ")
    print("4 for update github id ")
    print("5 for print information of friend.")
    print("6 for print information of all friends ")
    print("7 for read information of friends ")
    print("8 for exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter name : ")
        phone=input("Enter phone no : ")
        github=input("Enter github id : ")
        r=add(name,phone,github)
        if r:
            print("Friend added..")
        else:
            print("Friend not added..")
    elif choice==2:
        name=input("Enter name : ")
        phone=input("Enter phone no : ")
        github=input("Enter github id : ")
        r=remove(name,phone,github)
        if r:
            print("Friend removed..")
        else:
            print("Friend not removed..")
    elif choice==3:
        name=input("Enter name : ")
        phone=input("Enter new phone no : ")
        r=updatePhone(name,phone)
        if r:
            print("Friend phone no updated..")
        else:
            print("Friend phone not updated..")
    elif choice==4:
        name=input("Enter name : ")
        github=input("Enter new github id : ")
        r=updateGithub(name,github)
        if r:
            print("Friend github id updated..")
        else:
            print("Friend github id not updated..")
    elif choice ==5:
        name=input("Enter name : ")
        r=printByName(name)
        if r!=0:
            for i in r:
                print(i,end="")
        else:
            print("Friend not exist..")
    elif choice == 6:
        r=printAll()
        if len(r)>0:
            print(r)
        else:
            print("File is empty")
    elif choice == 7:
        r=readAll()
        if len(r)>0:
            print(r)
        else:
            print("File is empty")
    elif choice == 8:
        break
    else:
        print("Please enter correct choice.")




    