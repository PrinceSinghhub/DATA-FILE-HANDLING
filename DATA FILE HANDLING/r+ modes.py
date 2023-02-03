with open("r+.txt",'r+') as p:
    # todo first read and then write
    print(p.read())
    p.write("hello ji\n")
