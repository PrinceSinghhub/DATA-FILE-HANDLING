a=open("openfile.txt",'r')
# todo read a file
# this function print one time only one line
b=a.readline()
# using while loop
while b!='':
    print(b)
    b = a.readline()
a.close()