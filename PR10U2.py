file = open("file4.txt","r")
content = file.read()
content=content.replace("gujarat","gujrat")
file.close()
file = open("file4.txt","w")
file.write(content)
print("Content updated...")
file.close()


