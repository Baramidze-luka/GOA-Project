
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

    def loan(self,):
        print("so, you want to get a loan from us")


        bank=input("which bank would you like to get a loan from").capitalize

        while (bank not in self.Balance) or (bank not in ["TBC","GEORGIAN","GOA","SAQARTVELOS BANKI","TBC BANKI","GOA BANKI"]):
            print("sorry we only support GOA, TBC and GEORGIAN banks")
            bank=input("which bank would you like to get a loan from").capitalize


        loan_Type=input("ok, wouldyou like Consumer loan, car loan or business loan").lower

        while loan_Type not in ["Consumer loan"," car loan","business loan"]:
            print("sorry , either we dont support that kind of loans or you miss-spelled it")
            loan_Type=input("ok, wouldyou like Consumer loan, car loan or business loan").lower

        if loan_Type=="Consumer loan":
            print("ok, you have chosen consumer loan")
            amount=int(input("how much would you like to loan"))

            while amount>500000:
                print("we only give loans up to 500,000")
                amount = int(input("how much would you like to loan"))
        
            years= int(input("how long would you like to pay the loan"))
            while years not in range(1,16):
                print("sorry we only give loans for 1-15 years")
                years= input("how long would you like to pay the loan")
            
            
            if years in [1,2,3,4,5]:
                if amount <= 4500:
                    annual_rate = 0.12  #  წლიური განაკვეთი 12%
                if 4500 < amount <= 10000:
                    annual_rate = 0.09  # წლიური განაკვეთი 9%
                if 10000 < amount <= 50000:
                    annual_rate = 0.078  # წლიური განაკვეთი 7.8%
                if 50000 < amount <= 500000:
                    annual_rate = 0.018  # წლიური განაკვეთი 1.8%
            


            if years in [6,7,8,9,10]:
                if amount <= 4500:
                    annual_rate = 0.16  #  წლიური განაკვეთი 16%
                if 4500 < amount <= 10000:
                    annual_rate = 0.10  # წლიური განაკვეთი 10%
                if 10000 < amount <= 50000:
                    annual_rate = 0.08  # წლიური განაკვეთი 8%
                if 50000 < amount <= 500000:
                    annual_rate = 0.03  # წლიური განაკვეთი 3%

            if years in [11,12,13,14,15]:
                if amount <= 4500:
                    annual_rate = 0.2  #  წლიური განაკვეთი 20%
                if 4500 < amount <= 10000:
                    annual_rate = 0.13  # წლიური განაკვეთი 13%
                if 10000 < amount <= 50000:
                    annual_rate = 0.10  # წლიური განაკვეთი 10%
                if 50000 < amount <= 500000:
                    annual_rate = 0.04  # წლიური განაკვეთი 4%





            print("თქვენ გნებავთ "+str(amount)+" ლარის გატანა "+str(years)+" წლით.თქვენ  წლიური გადასახადი იქნება "+str(int(amount/years*(1+annual_rate)))+
                    ".თვიურად მოგიწევთ"+str(int(amount/years*(1+annual_rate)/12))+"სულ მოგიწევთ"+str(int(amount*(1+annual_rate)))+" ლარის გადახდა.")
            
        if loan_Type=="car loan":
            print("ok, you have chosen car loan")
            amount=int(input("how much would you like to loan"))

            while amount>500000:
                print("we only give (car) loans up to 500,000")
                amount = int(input("how much would you like to loan"))

                car_price=int(input("how much does the car cost"))
                while car_price>amount:
                    print("the car price cant be more than the loan amount")
                    car_price=int(input("how much does the car cost"))
                while amount-car_price>50000:
                    print("the difference between the car price and the loan amount cant be more than 50,000")
                    car_price=int(input("how much does the car cost"))
                
                years= int(input("how long would you like to pay the loan"))    
                while years not in range(1,16):
                    print("sorry we only give loans for 1-15 years")
                    years= input("how long would you like to pay the loan")

                if years in [1,2,3,4,5]:        
                    if amount <= 4500:
                        annual_rate = 0.20  #  წლიური განაკვეთი 20%
                    if 4500 < amount <= 10000:
                        annual_rate = 0.18  # წლიური განაკვეთი 25%
                    if 10000 < amount <= 50000:
                        annual_rate = 0.15  # წლიური განაკვეთი 15%
                    if 50000 < amount <= 500000:
                        annual_rate = 0.12  # წლიური განაკვეთი 12%
                    if 500000 < amount <= 5000000:
                        annual_rate = 0.09  # წლიური განაკვეთი 9%
                elif years in range(5,11):
                    if amount <= 4500:
                        annual_rate = 0.25  #  წლიური განაკვეთი 25%
                    elif 4500 < amount <= 10000:
                        annual_rate = 0.20
                    elif 10000 < amount <= 50000:
                        annual_rate = 0.18
                    elif 50000 < amount <= 500000:
                        annual_rate = 0.15
                    elif 500000 < amount <= 5000000:
                        annual_rate = 0.12
                elif years in range(11,16):
                    if amount <= 4500:
                        annual_rate = 0.30
                    elif 4500 < amount <= 10000:
                        annual_rate = 0.25
                    elif 10000 < amount <= 50000:
                        annual_rate = 0.20
                    elif 50000 < amount <= 500000:
                        annual_rate = 0.18
                    elif 500000 < amount <= 5000000:
                        annual_rate = 0.15
                print("თქვენ გნებავთ "+str(amount)+" ლარის გატანა "+str(years)+" წლით.თქვენ  წლიური გადასახადი იქნება "+str(int(amount/years*(1+annual_rate)))+
                    ".თვიურად მოგიწევთ"+str(int(amount/years*(1+annual_rate)/12))+"სულ მოგიწევთ"+str(int(amount*(1+annual_rate)))+" ლარის გადახდა.")
                
        if loan_Type=="business loan":
            print("ok, you have chosen business loan")
            amount=int(input("how much would you like to loan"))
            while amount<50000000:
                print("we only give (business) loans up from 50,000,000")
                amount = int(input("how much would you like to loan"))
            while(amount>500000000):
                print("we only give loans up to 500,000,000")
                amount = int(input("how much would you like to loan"))

            years= int(input("how long would you like to pay the loan"))
            while years not in range(15,31):
                print("sorry we only give loans for 15-30 years")
                years= input("how long would you like to pay the loan")
            
            if years in range(15,21):
                if amount <= 70000000:
                    annual_rate = 0.40  #  წლიური განაკვეთი 30%
                if 70000000< amount <= 150000000:
                    annual_rate = 0.32  # წლიური განაკვეთი 25%
                if 150000000 < amount <= 500000000:
                    annual_rate = 0.25  # წლიური განაკვეთი 20%
                if 500000000 < amount <= 5000000000:
                    annual_rate = 0.18  # წლიური განაკვეთი 15%
            elif years in range(21,26):
                if amount <= 70000000:
                    annual_rate = 0.45
                if 70000000< amount <= 150000000:
                    annual_rate = 0.40
                if 150000000 < amount <= 500000000:
                    annual_rate = 0.32
                if 500000000 < amount <= 5000000000:
                    annual_rate = 0.25
            elif years in range(26,31):
                if amount <= 70000000:
                    annual_rate = 0.50
                if 70000000< amount <= 150000000:
                    annual_rate = 0.45
                if 150000000 < amount <= 500000000:
                    annual_rate = 0.40
                if 500000000 < amount <= 5000000000:
                    annual_rate = 0.32
            print("თქვენ გნებავთ "+str(amount)+" ლარის გატანა "+str(years)+" წლით.თქვენ  წლიური გადასახადი იქნება "+str(int(amount/years*(1+annual_rate)))+
                    ".თვიურად მოგიწევთ"+str(int(amount/years*(1+annual_rate)/12))+"სულ მოგიწევთ"+str(int(amount*(1+annual_rate)))+" ლარის გადახდა.")




