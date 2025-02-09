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

def Start():
    while True:
        MyAccount = Account()
        while MyAccount.name is None:
            print("Welcome to the Bank!")
            print("1. Log In")
            print("2. Sign Up")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                Name = input("Enter your name: ")
                Password = input("Enter your password: ")
                Mail = input("Enter your e-mail: ")
                Lower = Mail.lower()
                while ("@gmail.com" not in Lower) and ("@mail.ru" not in Lower):
                    print("Invalid e-mail! try again")
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
                UserBank.Deposit(input("Enter your pin: "), input("Choose a bank: "), float(input("Enter the amount: ")))
            elif choice == "2":
                UserBank.Withdraw(input("Enter your pin: "), input("Choose a bank: "), float(input("Enter the amount: ")))
            elif choice == "3":
                UserBank.SeeBalance(input("Choose a bank: "))
            elif choice == "4":
                fullname = input("Enter your full name: ")
                id = input("Enter your ID: ")
                Bank = input("Choose a bank: ")
                Limit = float(input("Enter the limit: "))
                UserBank.createCard(fullname, id, Bank, Limit)
            elif choice == "5":
                UserBank.loan()
            elif choice == "6":
                MyAccount['data']['Balance'] = UserBank.Balance
                MyAccount['data']['Cards'] = UserBank.Cards
                MyAccount.LogOut()
                break
            else:
                print("Invalid choice!")
                continue

Start()