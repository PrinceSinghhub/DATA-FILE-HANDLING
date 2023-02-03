a=open("openfile.txt",'r')
# todo read a file
# this function print one time only one line
b=a.readline()
print(b)
# for the second line
b=a.readline()
print(b)
a.close()