with open("a+.txt",'a+') as pr:
    # this methode me jo bhi write hoga USKI BAD APPEND KRIGA kriga
    # in this case is methode me write ki baad cursur point end ,me hoga letter
    # ki thats why usko kuch nhi miliga and kuch nhi print kriga ye
    # todo position of cursure tell()
    print(pr.tell())
    pr.write("hello my name is codex coder\n")
    # todo position of cursure tell()
    print(pr.tell())
    # todo if we wnat to print w+ data then use seek() methode
    print(pr.read())