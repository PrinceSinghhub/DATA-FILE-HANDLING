a=open("writeline.txt",'w')
'''this function is used if we append list or 
tuple of string in file'''
name=["ajeet\n","khushi\n","prince\n"]
a.writelines(name)
a.close()