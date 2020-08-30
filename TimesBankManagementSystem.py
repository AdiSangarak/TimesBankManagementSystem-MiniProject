#Made by Aditya Kumar Gupta
import pickle
import os
class Account :
    name = ''
    balance=0
    pinNo = ""
    def createAccount(self):
        self.name = input("Input Full Name : ").lower()
        self.pinNo = input("Please Input a pin of your choice : ")
        self.balance = int(input("Please Input a value to deposit to start a account : "))
        if self.balance>0:
            print("---------------Account Created----------------")
        else:
            print("*****Invalid deposit amount*****")

    
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def writeAccountsFile(account) : 
    if os.path.exists('./database.data'):
        infile = open('database.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('database.data')
    else :
        oldlist = [account]
    outfile = open('newdatabase.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newdatabase.data', 'database.data')

    
def depositAndWithdraw(name1,PIN,dORw): 
    if os.path.exists('./database.data'):
        infile = open('database.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('database.data')
        for item in mylist :
            if item.name == name1 :
                    if item.pinNo==PIN:
                        if dORw == 'D' :
                            amount = int(input("Enter the amount to deposit : "))
                            item.balance += amount
                            print(amount,"Successfully Deposited")
                            print("-----Your account is updated-----")
                        elif dORw == 'W' :
                            amount = int(input("Enter the amount to withdraw : "))
                            if amount <= item.balance :
                                item.balance -=amount
                                print(amount,"Successfully Withdrawn")
                                print("-----Your account is updated-----")
                            else :
                                print("*****Not Enough Balance,can't withdraw*****")
                    else:
                        print('*****Invalid Pin No*****')
        outfile = open('newdatabase.data','wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('newdatabase.data', 'database.data')

    else:
        print("-*-*-No records to Search-*-*-")


def intro():
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")

def start():
    print("-------------------------------------")
    print(" ----Welcome to Times Bank---- ")
    intro()

def displayAll():
    if os.path.exists('./database.data'):
        infile = open('database.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print('Customer_Name={0} & Balance={1}'.format(item.name,item.balance))
        infile.close()
    else :
        print("Oops! No records to display in Bank")

def main():
    ch=-1
    num=0
    name=''
    pin=''
    start()
    while ch != 5:
        if ch != -1: 
            intro()
        ch = int(input("Select your choice number from the above menu : "))
        print("Choice number",ch,"is selected by the customer")
        if ch == 1:
            num = int(input("Number of Customers : "))
            if(num>0):
                for i in range(num):
                    writeAccount()
            else:
                print("Invalid Number of Customers")
        elif ch == 2:
            name = input("Input Full Name : ").lower()
            pin = input("Input Pin : ")
            depositAndWithdraw(name,pin, 'W')
        elif ch == 3:
            name = input("Input Full Name : ").lower()
            pin = input("Input Pin : ")
            depositAndWithdraw(name,pin, 'D')
        elif ch == 4:
            displayAll();
        elif ch == 5:
            print("..Times Bank Exiting...\nLooking Forward To Your Next Vist...")
            break
        else :
            print("*****Invalid choice*****")


if __name__ == '__main__':
    main()
