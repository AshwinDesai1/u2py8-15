import sys
file_handler=open(sys.argv[1],"r")
info = file_handler.read()
print("\n"+sys.argv[1]+" Content : \n"+info)
file_handler.close()

file_handler2=open(sys.argv[2],"w+")
file_handler2.write(info)

file_handler2.seek(0)
detail = file_handler2.read()
print("\n"+sys.argv[2]+" Content :\n "+detail)
file_handler2.close()