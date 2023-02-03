with open("w+.txt",'w+') as codex:
    codex.write("hello i am programmer")
    # todo position of cursure tell()
    print(codex.tell())
    # todo if we wnat to print w+ data then use seek() methode
    codex.seek(0)
    # todo position of cursure tell()
    print(codex.tell())
    print(codex.read())