a=open("openfile.txt",'r')
# todo read a file
# this function print one time only one line
b=a.readline()
# using for loop
for i in b:
    if b!=' ':
        print(b,end="")
        b=a.readline()
a.close()