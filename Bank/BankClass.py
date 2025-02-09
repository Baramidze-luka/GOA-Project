
# შექმენი კლასი/ტიპი როგორც int str bool და float.
# მიანიშნე მას თავისი ფუნქციები
class Bank():
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = 0.0

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
            card = input("Which card would you like to top up with: 1.VISA 2.MASTER CARD 3.AMEX:").strip()#რომელი ბარათით სურს თანხის შეტანა

            if card == "VISA":
                count = float(input("How much money do you want to deposit into the account:"))
                print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                break
            elif card == "MASTER CARD":
                count= float(input("How much money do you want to deposit into the account:"))
                print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                break
            elif card == "AMEX":
                count= float(input("How much money do you want to deposit into the account:"))
                print("The amount is in the account Thanks for using.")#რა თანხის შემოტანა უნდა მომხმარებელს)
                break
            else:
                 print("Invalid card, try again ")
             

        bal = input("Do you want to see your balance?: 1.Yes 2.No:").strip()
        
        if bal == "Yes":
             print("Your balance is: " + str(count))
        else:
             print("Thank you for using our service.")


             
        

        



    def Withdraw(self,Amount: float):
        pass
        