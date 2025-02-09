import json
from BankClass import Bank
from AccountClass import Account

# დავაიმპორტედ ჩვენი ფაილი რომელიც დევს სხვა ფოლდერში



def Start():
    while True:
        MyAccount = Account()
        while MyAccount.name == None:
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
                while ("@gmail.com" or "@mail.ru") not in Lower:
                    print("Invalid e-mail! try again")
                    Mail = input("Enter your e-mail: ")
                    Lower = Mail.lower()
                Answer = MyAccount.LogIn(input("Enter your name: "), input("Enter your password: "), input("Enter your e-mail: "))
                print(Answer)
            elif choice == "2":
                Answer = MyAccount.SignUp(input("Enter your name: "), input("Enter your password: "), input("Enter your e-mail: "))
                print(Answer)
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
                continue
        while True:
            UserBank = Bank()
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
                UserBank.createCard()
            elif choice == "5":
                UserBank.loan()
            elif choice == "6":
                MyAccount.LogOut()
                break
            else:
                print("Invalid choice!")
                continue

Start()
