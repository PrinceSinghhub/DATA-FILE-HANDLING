amount=[10000]
with open("atm data.txt",'r') as k:
    for i in k:
        amount.append(int(i))
l=len(amount)
prise=amount[l-1]
if prise<0 or prise ==0:
    print("go and bhek maging on rod and then come in")
print("OPeration\n1 cash\n 2 add money\n3 Check balance")
n=int(input('ENTER YOUR COMAND = '))
if prise>0:
    if n == 1:
        n = int(input('ENTER YOUR money = '))
        d = prise - n
        print("your available balance is = ", d)
        with open("atm data.txt", 'a') as k:
            a = str(d)
            k.write(a)
            k.write("\n")
if n == 2:
    n = int(input('ENTER YOUR money = '))
    d = prise + n
    print("your available balance is = ", d)
    with open("atm data.txt", 'a') as k:
        a = str(d)
        k.write(a)
        k.write("\n")
if n==3:
    print("The total balance is =", prise)


