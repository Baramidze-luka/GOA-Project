class Bank:
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = {
            "GOA BANK": 0.0,  # GOA BANK-ის საწყისი ბალანსი
            "TBC BANK": 0.0,  # TBC BANK-ის საწყისი ბალანსი
            "GEO BANK": 0.0,  # GEO BANK-ის საწყისი ბალანსი
        }

    # self აღნიშნავს თავის თავს ანუ ბანკს
    # წარმოიდგინე self როგორც კომპიუტერის ფაილი რომ მიხვიდე ბალანცის ფაილამდე უნდა ქნა self.Balance

    def SeeBalance(self, bank_name: str):
        print(f"Your balance is: {self.Balance[bank_name]}")  # ბალანსის ჩვენება

    def Deposit(self, pin: str, bank: str, amount: float):
        # მომხმარებლის პინის შემოწმება

        # შეამოწმე მომხმარებლის პინ კოდი თუ სწორია.
        # ამას მერე დავამატებ

        # რომელი ბანკის არჩევა უნდა
        if bank == "1":
            bank_name = "GOA BANK"
            print("Welcome to GOA BANK")  # GOA BANK-ში მისალმება
        elif bank == "2":
            bank_name = "GEO BANK"
            print("Welcome to GEO BANK")  # GEO BANK-ში მისალმება
        elif bank == "3":
            bank_name = "TBC BANK"
            print("Welcome to TBC BANK")  # TBC BANK-ში მისალმება
        else:
            print("Error: Invalid bank")  # არასწორი ბანკი
            return

        # თანხის შეტანა
        self.Balance[bank_name] += amount
        print("The amount is in the account. Thanks for using.")  # თანხა შეტანილია ანგარიშზე

    def Withdraw(self, pin: str, bank: str, amount: float):
        # მომხმარებლის პინის შემოწმება

        # TODO
        # შეამოწმე მომხმარებლის პინ კოდი თუ სწორია.
        # ამას მერე დავამატებ
    
        # რომელი ბანკიდან სურს თანხის გამოტანა
        if bank == "1":
            bank_name = "GOA BANK"
            print("Welcome to GOA BANK")  # GOA BANK-ში მისალმება
        elif bank == "2":
            bank_name = "GEO BANK"
            print("Welcome to GEO BANK")  # GEO BANK-ში მისალმება
        elif bank == "3":
            bank_name = "TBC BANK"
            print("Welcome to TBC BANK")  # TBC BANK-ში მისალმება
        else:
            print("Error: Invalid bank")  # არასწორი ბანკი
            return

        # თანხის გამოტანა
        if self.Balance[bank_name] >= amount:
            self.Balance[bank_name] -= amount  # თანხის გამოტანა
            print(f"{amount} The amount was successfully withdrawn from {bank_name}.")  # თანხის წარმატებული გამოტანა
        else:
            print("Insufficient funds in the account.")  # არასაკმარისი თანხა ანგარიშზე

