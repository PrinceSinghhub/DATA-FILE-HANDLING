with open("name.txt","w") as p:
    p.write("Ajeet\n")
    p.write("khushi\n")
    p.write("codex\n")
    p.write("coder\n")
    p.write("aj\n")

with open("age.txt","w") as p:
    p.write("codex = 18\n")
    p.write("khushi = 17\n")
    p.write("coder = 12\n")
    p.write("aj = 20\n")
    p.write("Ajeet = 18\n")

with open("id.txt","w") as p:
    p.write("khushi = 102\n")
    p.write("codex = 103\n")
    p.write("Ajeet = 101\n")
    p.write("coder = 104\n")
    p.write("aj = 105\n")
with open("name.txt",'r') as pr:
    n=input("Enter Name: ")
    for i in pr:
        if n in i:
            with open("age.txt","r") as a:
                for i in a:
                    if n in i:
                        x=i
                        y=''
                        for i in x:
                            if i.isdigit():
                                y=y+i
                with open("id.txt",'r') as k:
                    for i in k:
                        if n in i:
                            d=i
                            aj = ''
                            for k in d:
                                if k.isdigit():
                                    aj+=k
                            e,f,g=n,y,aj
                            print(f"Name: {e} age: {f} id: {g}")
                            with open("newdata.txt",'w') as kj:
                                kj.write(e)
                                kj.write("\n")
                                kj.write(f)
                                kj.write("\n")
                                kj.write(g)
                                kj.write("\n")


