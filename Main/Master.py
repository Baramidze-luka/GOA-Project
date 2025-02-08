from Bank.BankClass import *

# დავაიმპორტედ ჩვენი ფაილი რომელიც დევს სხვა ფოლდერში

Bank = Bank()

Bank.Deposit(150.0)
Bank.Withdraw(100.0)
print(Bank.Balance)