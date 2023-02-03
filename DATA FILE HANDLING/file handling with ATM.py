print("=====================================================================================")
print("                            WELCOME TO ATM MECHINE                                   ")
print("=====================================================================================")
import time

print("please insert your card")
time.sleep(1)
print("======================================================================================")
balance = [10000]
with open("ajeet ATM DATA.txt",'r') as p:
    for i in p:
        balance.append(int(i))
l=len(balance)
balance=balance[l-1]
pin = int(input("please enter a pin no"))
while True:
    if (pin == 1234):
        print('''
                 1 check balance
                 2 deposite
                 3 widhdawal
                 4 mini statement
                 5 trasfers
                 6 exist ''')
        print("======================================================================================")

        option = int(input("please choose option"))
        if (option == 1):
            print("your balance is :", balance)
            print("====================================================================================")
        elif (option == 2):
            amount = int(input("please enter amount"))
            print("========================================================================")
            print("deposite is successful")
            balance = balance + amount
            with open("ajeet ATM DATA.txt",'a') as p:
                  a=str(balance)
                  p.write(a)
            with open("ajeet ATM DATA.txt",'a') as p:
                p.write("\n")
            print("aviable balance:", balance)
        elif (option == 3):
            amount = int(input("please enter amount"))
            balance = balance - amount
            with open("ajeet ATM DATA.txt",'a') as p:
                  a=str(balance)
                  p.write(a)
            with open("ajeet ATM DATA.txt",'a') as p:
                p.write("\n")
            print("your widhdawal is successful")
            print("aviable balance", balance)
            print("=========================================================================")
        elif (option==4):
            print("YOUR MINI STATEMENT IS ")
            with open("ajeet ATM DATA.txt",'r') as p:
                  print(p.read())

        elif (option == 5):
            print("1 account       2 mobile no")
            option = int(input("please choose option"))
            if (option == 1):
                account = int(input("please enter a account number"))
                if (account == 123456789):
                    fs = input("please enter a IFSC CODE")
                    if (fs == "SBIN0004654"):
                        amount = int(input("please enter amount"))
                        balance = balance - amount
                        with open("ajeet ATM DATA.txt", 'a') as p:
                            a = str(balance)
                            p.write(a)
                        with open("ajeet ATM DATA.txt", 'a') as p:
                            p.write("\n")
                        print("your transfers is successfull")
                        print("aviable balance", balance)
                        print(
                            "==========================================================================================")
                    else:
                        print("wrong ifsc code")
            elif (option == 2):
                mobile = int(input("please enter a mobile no"))
                if (mobile == 9905844672):
                    amount = int(input("please enter amount"))
                    balance = balance - amount
                    with open("ajeet ATM DATA.txt", 'a') as p:
                        a = str(balance)
                        p.write(a)
                    with open("ajeet ATM DATA.txt", 'a') as p:
                        p.write("\n")
                    print("your transfers is successfull")
                    print("avible balance", balance)
                    print("=============================================================================")
                else:
                    print("wrong account no")
            else:
                print("invaild option")

        elif (option == 6):
            break
        else:
            print("invild option try again")
            break
    else:
        print("wronge pin try again")
        break


