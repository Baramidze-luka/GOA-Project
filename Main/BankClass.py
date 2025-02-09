import time
import random
import json

# JSON ფაილის გზის განსაზღვრა
PathToFileJson = os.path.join(os.path.dirname(__file__), 'Cards.json')

class Bank:
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = {
            "GOA BANK": 0.0,  # GOA BANK-ის საწყისი ბალანსი
            "TBC BANK": 0.0,  # TBC BANK-ის საწყისი ბალანსი
            "GEO BANK": 0.0,  # GEO BANK-ის საწყისი ბალანსი
        }
        self.Cards = {

        }  # ბანკის ბარათები

    # self აღნიშნავს თავის თავს ანუ ბანკს
    # წარმოიდგინე self როგორც კომპიუტერის ფაილი რომ მიხვიდე ბალანცის ფაილამდე უნდა ქნა self.Balance

    def SeeBalance(self, bank_name: str):
        if not bank_name in self.Balance:
            print("Error: Invalid bank")
            return
        print(f"Your balance is: {self.Balance[bank_name]}")  # ბალანსის ჩვენება

    def Deposit(self, pin: str, CardNum: str,CVV: str,Expiration:str, amount: float):
        Card = self.Cards[CardNum]
        if not Card: print("invalid card"); return
        if Card["CVV"] != CVV: print("Incorrect CVV");  return
        if Card["Expire Date"] != Expiration:  print("Incorrect Expiration Date"); return 
        if Card["Pin"] != pin: print("Incorrect Pin"); return

        if Card["Balance"] < amount: print("Insufficient funds in the card."); return

        if amount > Card["Limit"]: print("Amount exceeds the limit"); return

        if Card["Bank"] == "GOA BANK":
            Card["Balance"] -= amount
            self.Balance["GOA BANK"] += amount
            print(f"{amount} was successfully deposited to GOA BANK.")
        elif Card["Bank"] == "GEO BANK":
            Card["Balance"] -= amount
            self.Balance["GEO BANK"] += amount
            print(f"{amount} was successfully deposited to GEO BANK.")
        elif Card["Bank"] == "TBC BANK":
            Card["Balance"] -= amount
            self.Balance["TBC BANK"] += amount
            print(f"{amount} was successfully deposited to TBC BANK.")
        else:
            print("Error: Invalid bank")
        
    def Deposit(self, pin: str, CardNum:str,Bank:str, amount: float):
        Card = self.Cards[CardNum]
        Bank = self.Balance[Bank]
        if not Card: print("invalid card"); return
        if Card["Pin"] != pin: print("Incorrect Pin"); return

        if Bank < amount: print("Insufficient funds in the Balance."); return

        if Bank == "GOA BANK":
            Card["Balance"] += amount
            self.Balance["GOA BANK"] -= amount
            print(f"{amount} was successfully deposited to GOA BANK.")
        elif Card["Bank"] == "GEO BANK":
            Card["Balance"] += amount
            self.Balance["GEO BANK"] -= amount
            print(f"{amount} was successfully deposited to GEO BANK.")
        elif Card["Bank"] == "TBC BANK":
            Card["Balance"] += amount
            self.Balance["TBC BANK"] -= amount
            print(f"{amount} was successfully deposited to TBC BANK.")
        else:
            print("Error: Invalid bank")
        

    def createCard(self,fullname : str, id:str,bank : str,Limit:float):
        if len(id) != 11:
            print("Error: Invalid ID")
            return
        if not id.isdigit():
            print("Error: Invalid ID")
            return
        if not fullname.isalpha():
            print("Error: Invalid Name")
            return
        Current = time.localtime()
        print(Current)
        print(Current.tm_year + 3)

        CardNum = ""

        for i in range(4):
            CardNum += str(random.randint(1000, 9999))
            if i != 3:
                CardNum += "-"
        CardExists = False
        cards = None
        with open(PathToFileJson, 'r') as file:
            cards = json.load(file)
            if CardNum in cards:
                print("Error: Card already exists")
                CardExists = True
                return
            
        while CardExists:
            CardNum = ""
            for i in range(4):
                CardNum += str(random.randint(1000, 9999))
                if i != 3:
                    CardNum += "-"
            if CardNum not in cards:
                CardExists = False

        CVV = str(random.randint(100, 999))
        Pin = str(random.randint(1000, 9999))
        card = {
            "Full Name": fullname,
            "ID": id,
            "Expire Date": f"{Current.tm_year + 3}-{Current.tm_mon}-{Current.tm_mday}",
            "CVV": CVV,
            "Pin": Pin,
            "Bank": bank,
            "Balance": 0.0,
            "Limit": Limit,
        }
        self.Cards[CardNum] = card
        print(f" your card is: {card}")
