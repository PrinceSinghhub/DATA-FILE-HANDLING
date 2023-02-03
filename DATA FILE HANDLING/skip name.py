with open("skip.txt",'w') as kp:
    kp.write("CODEX CODER\n")

with open("skip.txt",'r+') as p:
    d=p.read()
    d1=len(d)
    for i in range(2,d1):
        c=d[i]
        p.write(c)
