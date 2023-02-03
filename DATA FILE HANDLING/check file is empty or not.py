import os
b=True
a=os.stat("empty file.txt").st_size==0
f=os.path.getsize("empty file.txt")
if b==a:
    print("Yes this file is Empty")
    print("the size of file is =",f,"bytes")

# todo second methoe
f=os.path.getsize("empty file.txt")
if f==0:
    print("Yes this file is Empty")
    print("the size of file is =", f, "bytes")
if f>0:
    print("No this file is Not Empty")
    print("the size of file is =", f, "bytes")

# todo third methode
with open("empty file.txt",'r') as p:
    a=p.read()
    if a!='':
        print("file is not empty")
    else:
        print("file is empty")