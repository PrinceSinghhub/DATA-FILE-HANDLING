a=open("mechinical.txt",'r')
b=a.read()
a.close()
with open("b tech.txt",'a') as kp:
    kp.write(b)