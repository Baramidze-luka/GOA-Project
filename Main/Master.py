import json
import sys
import os

# დავამატოთ ფაილის გზა
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Bank')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Login')))

from BankClass import Bank
from AccountClass import Account

# დავაიმპორტედ ჩვენი ფაილი რომელიც დევს სხვა ფოლდერში
UserBank = Bank()
MyAccount = Account()

def autofill_card():
    print("Would you like to autofill card details? If yes, press 1. If no, press 2.")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Choose a card: ")
        for i in range(len(MyAccount.user['data']['AutoFill']['Cards'])):
            print(f"{i + 1}. {MyAccount.user['data']['AutoFill']['Cards'][i]}")
        choice = int(input("Choose an option: "))
        Card = MyAccount.user['data']['AutoFill']['Cards'][choice - 1]
        Num = Card["Card Number"]
        ExpireDate = Card["Expire Date"]
        cvv = Card["CVV"]
        return Num, cvv, ExpireDate
    elif choice == "2":
        return None, None, None
    else:
        print("Invalid choice!")
        return None, None, None

def autofill_personal_data():
    print("Would you like to autofill personal data? If yes, press 1. If no, press 2.")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Choose a personal data entry: ")
        if len(MyAccount.user['data']['AutoFill']['PersonalData']) == 0: print("there is no personal data autofill"); return None, None
        for i in range(len(MyAccount.user['data']['AutoFill']['PersonalData'])):
            print(f"{i + 1}. {MyAccount.user['data']['AutoFill']['PersonalData'][i]}")
        choice = int(input("Choose an option: "))
        PersonalData = MyAccount.user['data']['AutoFill']['PersonalData'][choice - 1]
        fullname = PersonalData["Full Name"]
        id = PersonalData["ID"]
        return fullname, id
    elif choice == "2":
        return None, None
    else:
        print("Invalid choice!")
        return None, None

def AccountOption():
    while MyAccount.name is None:
        print("Welcome to the Bank!")
        print("1. Log In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            Name = input("Enter your name: ")
            while len(Name) < 3:
                print("Name should be at least 3 characters long")
                Name = input("Enter your name: ")
            Password = input("Enter your password: ")
            while len(Password) < 6:
                print("Password should be at least 6 characters long")
                Password = input("Enter your password: ")
            while "@#$%^&*()_+" not in Password:
                print("Password should contain at least one special character")
                Password = input("Enter your password: ")
                continue
            while "1234567890" not in Password:
                print("Password should contain at least one number")
                Password = input("Enter your password: ")
            while not any(char.isupper() for char in Password):
                print("Password should contain at least one uppercase letter")
                Password = input("Enter your password: ")
            Mail = input("Enter your e-mail: ")
            Lower = Mail.lower()
            while ("@gmail.com" not in Lower) and ("@mail.ru" not in Lower):
                print("Invalid e-mail! try again. Email Must contain @gmail.com or @mail.ru")
                Mail = input("Enter your e-mail: ")
                Lower = Mail.lower()
            Answer = MyAccount.LogIn(Name, Password, Mail)
            print(Answer)
        elif choice == "2":
            Answer = MyAccount.SignUp(input("Enter your name: "), input("Enter your password: "), input("Enter your e-mail: "))
            print(Answer)
        elif choice == "3":
            return  # გამოვიდეთ პროგრამიდან
        else:
            print("Invalid choice!")
            continue

def initializeBank():
    while True:
        if MyAccount.user['data']['Balance']:
            UserBank.Balance = MyAccount.user['data']['Balance']
            if MyAccount.user['data']['Cards']:
                UserBank.Cards = MyAccount.user['data']['Cards']
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Create Card")
            print("5. Take a Loan")
            print("6. Log Out")
            choice = input("Choose an option: ")
            if choice == "1":
                if len(MyAccount.user['data']['AutoFill']['Cards']) > 0:
                    Num, cvv, ExpireDate = autofill_card()
                    if Num:
                        UserBank.Deposit(input("Enter your pin: "), Num, cvv, ExpireDate, input("Choose a bank: "), float(input("Enter the amount: ")))
                    else:
                        UserBank.Deposit(input("Enter your pin: "), input("Enter Card Number"), input("Enter CVV"), input("Enter Expiration Date"), input("Choose a bank: "), float(input("Enter the amount: ")))
                else:
                    UserBank.Deposit(input("Enter your pin: "), input("Enter Card Number"), input("Enter CVV"), input("Enter Expiration Date"), input("Choose a bank: "), float(input("Enter the amount: ")))
            elif choice == "2":
                if len(MyAccount.user['data']['AutoFill']['Cards']) > 0:
                    Num, cvv, ExpireDate = autofill_card()
                    if Num:
                        UserBank.Withdraw(input("Enter your pin: "), Num, input("Choose a bank: "), float(input("Enter the amount: ")))
                    else:
                        UserBank.Withdraw(input("Enter your pin: "), input("Enter Card Number"), input("Choose a bank: "), float(input("Enter the amount: ")))
                else:
                    UserBank.Withdraw(input("Enter your pin: "), input("Enter Card Number"), input("Choose a bank: "), float(input("Enter the amount: ")))
            elif choice == "3":
                UserBank.SeeBalance(input("Choose a bank: "))
            elif choice == "4":
                fullname, id = autofill_personal_data()
                if not fullname:
                    fullname = input("Enter your full name: ")
                if not id:
                    id = input("Enter your ID: ")
                Bank = input("Choose a bank: ")
                Limit = float(input("Enter the limit: "))
                Card = UserBank.createCard(fullname, id, Bank, Limit)
                print("Would you like to add card and personal data to autofill? If yes, press 1. If no, press 2.")
                choice = input("Choose an option: ")
                if choice == "1":
                    MyAccount.user['data']['AutoFill']['Cards'].append(Card)
                    MyAccount.user['data']['AutoFill']['PersonalData'].append({"Full Name": fullname, "ID": id})
            elif choice == "5":
                UserBank.loan()
            elif choice == "6":
                MyAccount.user['data']['Balance'] = UserBank.Balance
                MyAccount.user['data']['Cards'] = UserBank.Cards
                MyAccount.LogOut()
                Start()
                return
            else:
                print("Invalid choice!")
                continue

def Start():
    AccountOption()
    initializeBank()

Start()