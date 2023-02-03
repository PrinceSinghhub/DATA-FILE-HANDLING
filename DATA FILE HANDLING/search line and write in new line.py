with open("check.txt",'w') as p:
    p.write("name           roll no        age\n")
    p.write("khushi         1001           15\n")
    p.write("ajeet          5005           200\n")
    p.write("codex coder     07            18\n")

with open("check.txt",'r') as p:
    with open("search data.txt","a") as p1:
        n=input("Enter command = ")
        a=p.readline()
        while a != '':
            if n in a:
                p1.write(a)
            a = p.readline()
# todo second methode
# with open("check.txt",'r') as p:
#     n=input("command = ")
#     with open("search data.txt", 'w') as p1:
#         for i in p:
#             if n in i:
#                 p1.write(i)









