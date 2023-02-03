with open("dictionary.txt",'a') as p:
    x={'1000':"1/1/2002",'20000':"02/08/2021"}
    d=x.items()
    d1=str(d)
    p.write(d1)
