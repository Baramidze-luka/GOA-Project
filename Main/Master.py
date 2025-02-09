
from BankClass import Bank
from AccountClass import Account

# დავაიმპორტედ ჩვენი ფაილი რომელიც დევს სხვა ფოლდერში

UserBank = Bank()

def Start():
    print("Welcome to the Bank!")
    print("1. Log In")
    print("2. Sign Up")
    print("3. Exit")
    choice = input("Choose an option: ")
    MyAccount = Account()
    if choice == "1":
        Name = input("Enter your name: ")
        Password = input("Enter your password: ")
        Mail = input("Enter your e-mail: ")
        Lower = Mail.lower()
        if ("@gmail.com" or "@mail.ru") not in Lower:
            print("Invalid e-mail!")
            Start()
    elif choice == "2":
        Answer = MyAccount.SignUp(input("Enter your name: "), input("Enter your password: "), input("Enter your e-mail: "))
        print(Answer)
    elif choice == "3":
        return
    else:
        print("Invalid choice!")
        Start()

Start()