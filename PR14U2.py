import re
data='''
   mobile no 1 : 9090887889
   mobile no 2 : 998-432-5721
   mobile no 3 : (342)-783-7860
'''

pattern = r"\(?\d{3}\)?-?\d{3}-?\d+"
print(pattern)
find = re.findall(pattern,data)
for i in find:
    print(i) 