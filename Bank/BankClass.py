class Bank():
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = {
            "GOA BANK": 0.0,
            "TBC BANK": 0.0,
            "GEO BANK": 0.0,
        }

    # self აღნიშნავს თავის თავს ანუ ბანკს
    # წარმოიდგინე self როგორც კომპიუტერის ფაილი რომ მიხვიდე ბალანცის ფაილამდე უნდა ქნა self.Balance

    # Amount : float არის type check რომელიც გადააქცევს მოცემულ არგუმენტს იმ ტიპად რასაც აძლევ
    # () -> bool: აღნიშნავს რომ ფუნქცია დააბრუნებს boolean ტიპს

    # ფუნქცია აბრუნებს როცა მასში არის გამოყენებული return

    # def Deposit(self,Amount : float) -> bool:
    #     return True

    # Answer = Deposit() რომელიც მომცემს True'ს
    # როგორც Input = input() გვაძლევს სტრინგს ეს არის პასუხი return ის გამოყენებით  

    def Deposit(self):
                    pin = input("Create Your Pin:")
                            
                    while True:
                                enter = input("Enter Your Pin:")
                                if enter == pin:
                                        print("You have successfully logged in.")
                                        break
                                elif enter != pin:
                                        print("The pincode is incorrect.")
                    
                    while True:
                        bank = input("Which bank would you like to deposit the money at: 1.GOA BANK,2.GEO BANK,3.TBC BANK:").strip()#რომელი ბანკის არჩევა უნდა
                        if bank == "GOA BANK":
                            print("Welcome to GOA BANK")
                            break
                        elif bank == "TBC BANK":
                            print("Welcome to TBC BANK")
                            break
                            
                        elif bank == "GEO BANK":
                            print("Welcome to GEO BANK")
                            break
                        else:
                            print("Error: Invalid bank")
                        
                    while True:
                        card = input("Which card would you like to top up with: 1.GOA BANK CARD 2.GEO BANK CARD 3.TBC BANK CARD:").strip()#რომელი ბარათით სურს თანხის შეტანა

                        if card == "GOA BANK CARD":
                            self.balance = float(input("How much money do you want to deposit into the account:"))
                            self.Balance["GOA BANK"] += self.balance
                            print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                            break
                        elif card == "GEO BANK CARD":
                            self.balance = float(input("How much money do you want to deposit into the account:"))
                            self.Balance["GEO BANK"] += self.balance
                            print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                            break
                        elif card == "TBC BANK CARD":
                            self.balance = float(input("How much money do you want to deposit into the account:"))
                            self.Balance["TBC BANK"] += self.balance
                            print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                            break
                        else:
                            print("Invalid card, try again ")
                        

                    bal = input("Do you want to see your balance?: 1.Yes 2.No:").strip()
                    
                    if bal == "Yes":
                        print("Your balance is: " + str(self.balance))
                    else:
                        print("Thank you for using our service.")

    def Withdraw(self):
        pin = input("Create Your Pin:")
                            
        while True:
            enter = input("Enter Your Pin:")
            if enter == pin:
                print("You have successfully logged in.")
                break
            elif enter != pin:
                print("The pincode is incorrect.")
                
        
        while True:
                    bank = input("Which bank would you like to withdraw money from? 1.GOA Bank, 2.GEO Bank, 3.TBC Bank:").strip()
                    if bank in self.Balance:
                        print(f"Welcome {bank}")
                        break
                    else:
                        print("Error: Invalid bank")
        while True:
            card = input("Which card would you like to withdraw money from?: 1.GOA BANK CARD 2.GEO BANK CARD 3.TBC BANK CARD:").strip()
            if card in ["GOA BANK CARD", "GEO BANK CARD", "TBC BANK CARD"]:
                amount = float(input("How much money do you want to withdraw from the account?:"))
                if self.Balance[bank] >= amount:
                    self.Balance[bank] -= amount  # თანხის გამოტანა
                    print(f"{amount} The amount was successfully withdrawn. {bank} From Garish.")
                    break
                else:
                    print("Insufficient funds in the account.")
                    break
            else:
                print("Invalid card, try again.")                       

account = Bank()
account.Deposit()
account.Withdraw()
    
def Deposit(self,Amount : float,Bank:str):
        self.Balance[Bank] += Amount

def Withdraw(self,Amount: float,Bank:str):
        self.Balance[Bank] += Amount
