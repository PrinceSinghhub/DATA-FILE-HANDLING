with open("w+.txt",'w+') as codex:
    # todo first write and then read
    # this methode me jo bhi write hoga eache time override kriga
    # in this case is methode me write ki baad cursur point end ,me hoga letter
    # ki thats why usko kuch nhi miliga and kuch nhi print kriga ye
    # todo position of cursure tell()
    print(codex.tell())
    codex.write("my name is codex coder")
    # todo after reading tell
    print((codex.tell()))
    # todo if we wnat to print w+ data then use seek() methode
    print(codex.read())