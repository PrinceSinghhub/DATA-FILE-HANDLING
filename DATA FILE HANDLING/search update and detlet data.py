# todo write data
with open("SUD.txt",'w+') as p:
    p.write("name           roll no        age\n")
    p.write("khushi         1001           150\n")
    p.write("ajeet          5005           2002\n")
    p.write("codex coder     07            18\n")

# todo check data or search
n=input("Enter name = ")
with open('SUD.txt','r') as p:
    for i in p:
        if n in i:
            print("Yes Data found in our data base")
            print(i)
            break

# todo delet data
n=input("Enter name = ")
with open('SUD.txt','r') as p:
    for i in p:
        if n in i:
            continue
        print(i)

# todo update data
n=input("command = ")
with open("SUD.txt",'r') as p:
    with open("update.txt",'w') as p1:
        for i in p:
            if n in i:
                n = input("data command = ")
                p1.write(n)
                p1.write("\n")
                continue
            p1.write(i)

