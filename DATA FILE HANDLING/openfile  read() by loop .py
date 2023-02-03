a=open("openfile.txt",'r')
# todo read a file
b=a.read()
for i in b:
    print(i*2,end="")
a.close()