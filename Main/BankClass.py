import time
import random
import json
import os
import math


def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_test_case_input(json_data, difficulty, task_name):
    return json_data[difficulty][task_name]['TestCases']

# JSON ფაილის გზის განსაზღვრა
PathToFileJson = os.path.join(os.path.dirname(__file__), 'Cards.json')
PathToProgrammingJobJson = os.path.join(os.path.dirname(__file__), 'ProggrammingJob.json')


class Bank:
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = {
            "GOA BANK": 0.0,  # GOA BANK-ის საწყისი ბალანსი
            "TBC BANK": 0.0,  # TBC BANK-ის საწყისი ბალანსი
            "GEO BANK": 0.0,  # GEO BANK-ის საწყისი ბალანსი
        }
        self.Cards = {}  # ბანკის ბარათები
        self.Loans = [
            
        ]

    # self აღნიშნავს თავის თავს ანუ ბანკს
    # წარმოიდგინე self როგორც კომპიუტერის ფაილი რომ მიხვიდე ბალანცის ფაილამდე უნდა ქნა self.Balance

    def SeeBalance(self, bank_name: str):
        bank_name.upper()
        if bank_name not in self.Balance:
            print("Error: Invalid bank")
            return
        print(f"Your balance is: {self.Balance[bank_name]}")  # ბალანსის ჩვენება

    def Deposit(self, pin: str, CardNum: str, CVV: str, Expiration: str,Bank:str, amount: float):
        Bank.upper()
        Card = self.Cards.get(CardNum)
        if not Card:
            print("Invalid card")
            return
        if Card["CVV"] != CVV:
            print("Incorrect CVV")
            return
        if Card["Expire Date"] != Expiration:
            print("Incorrect Expiration Date")
            return
        if Card["Pin"] != pin:
            print("Incorrect Pin")
            return
        if Card["Balance"] < amount:
            print("Insufficient funds in the card.")
            return
        if amount > Card["Limit"]:
            print("Amount exceeds the limit")
            return

        if Bank == "GOA BANK":
            Card["Balance"] -= amount
            self.Balance["GOA BANK"] += amount
            print(f"{amount} was successfully deposited to GOA BANK.")
        elif Bank == "GEO BANK":
            Card["Balance"] -= amount
            self.Balance["GEO BANK"] += amount
            print(f"{amount} was successfully deposited to GEO BANK.")
        elif Bank == "TBC BANK":
            Card["Balance"] -= amount
            self.Balance["TBC BANK"] += amount
            print(f"{amount} was successfully deposited to TBC BANK.")
        else:
            print("Error: Invalid bank")

    def Withdraw(self, pin: str, CardNum: str, Bank: str, amount: float):
        Bank.upper()
        Card = self.Cards.get(CardNum)
        if not Card:
            print("Invalid card")
            return
        if Card["Pin"] != pin:
            print("Incorrect Pin")
            return
        if self.Balance[Bank] < amount:
            print("Insufficient funds in the Balance.")
            return

        if Bank == "GOA BANK":
            Card["Balance"] += amount
            self.Balance["GOA BANK"] -= amount
            print(f"{amount} was successfully withdrawn from GOA BANK.")
        elif Bank == "GEO BANK":
            Card["Balance"] += amount
            self.Balance["GEO BANK"] -= amount
            print(f"{amount} was successfully withdrawn from GEO BANK.")
        elif Bank == "TBC BANK":
            Card["Balance"] += amount
            self.Balance["TBC BANK"] -= amount
            print(f"{amount} was successfully withdrawn from TBC BANK.")
        else:
            print("Error: Invalid bank")

    def createCard(self, fullname: str, id: str, bank: str, Limit: float) -> dict:
        bank.upper()
        if len(id) != 11 or not id.isdigit():
            print("Error: Invalid ID")
            return
        AlphaName = fullname.replace(" ", "")
        if not AlphaName.isalpha():
            print("Error: Invalid Name")
            return

        Current = time.localtime()
        CardNum = ""
        for i in range(4):
            CardNum += str(random.randint(1000, 9999))
            if i != 3:
                CardNum += "-"
        cards = None
        with open(PathToFileJson, 'r') as file:
            cards = json.load(file)
            while CardNum in cards:
                print("Error: Card already exists")
                CardNum = ""
                for i in range(4):
                    CardNum += str(random.randint(1000, 9999))
                    if i != 3:
                        CardNum += "-"

        cards[CardNum] = CardNum
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
            "Card Number": CardNum,
        }
        self.Cards[CardNum] = card
        print("Your card has been successfully created.")
        print(f"Card Number: {CardNum}")
        for key, value in card.items():
            print(f"{key}: {value}")
        return card
    
    def Work(self):
        # ეკრანზე გამოვიტანთ შეტყობინებას, რომ მომხმარებელმა აირჩიოს ფულის გამომუშავების მეთოდი
        print("Choose a way to make money")  
        print("1. Programming")  

        # მომხმარებელს ვთხოვთ აირჩიოს ვარიანტი
        choice = input("Choose an option: ")  
        
        # თუ მომხმარებელმა აირჩია პროგრამირება
        if choice == "1":  
            print("Difficulty Doesnt Have Any Tasks, Choose Difficulty")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            difficulty = input("Choose an option: ")

            DifficultyDict = {
                "1":  "Easy",
                "2":  "Medium",
                "3":  "Hard"
            }

            # Load JSON data
            json_data = load_json_data(PathToProgrammingJobJson)
            # Extract inputs for the task

            while len(json_data[(DifficultyDict[difficulty])]) == 0:
                print("Chosen Difficulty Doesnt Have Any Tasks, Please Choose Another Difficulty")
                print("1. Easy")
                print("2. Medium")
                print("3. Hard")
                difficulty = input("Choose an option: ")



            task_key = random.choice(list(json_data[(DifficultyDict[difficulty])].keys()))  # Pick a random key
            

            task = json_data[DifficultyDict[difficulty]][task_key]  # Get the corresponding task dictionary
            print(task_key)
            print(task['Description'])
            print(f"Reward {task['Reward']}$")

            print("Tip: If you have to return multiple values return all values in a list")

            def Run(Func, *args, expected) -> bool:
                print(expected)
                try:
                    result = Func(*args)
                    print(result)
                    if isinstance(expected, list) or isinstance(expected, tuple):
                        if result == expected:
                            return True
                        else:
                            return False
                    else:
                        if result == expected:
                            return True
                        else:
                            return False
                except Exception as e:
                    print("Error:", e)
                    return False

            # ვქმნით ფუნქციის შაბლონს, სადაც კოდი ჩაიწერება დინამიურად
            WholeCode = f"def func({task["Input"]}):\n"  

            # მომხმარებელს ვეუბნებით, რომ შეუძლია დაამატოს კოდი და "e"-თი დაასრულოს შეყვანა
            print("Type e to end the code")  
            print(f"def func({task["Input"]}):")  

            # ცვლადი, რომელიც განსაზღვრავს, რამდენი ინტენდაცია (TAB ან 4 space) უნდა იყოს  
            indentation_level = 1  

            # ციკლი, რომელიც მომხმარებელს აძლევს საშუალებას შეიყვანოს კოდი ხაზი-ხაზად
            while True:  
                Line = input("    " * indentation_level)  # მომხმარებლის შეყვანილი კოდი  
                
                if Line == "e":  # თუ შეყვანილია "e", ვწყვეტთ კოდის შეყვანას  
                    break  

                stripped = Line.strip()  # წაშლის ცარიელი ადგილები (whitespace) ხაზის თავში და ბოლოში  

                # თუ ხაზი ბოლოვდება ":", ეს ნიშნავს რომ საჭიროა შიდა ბლოკი (მაგალითად if, for, while, def)
                if stripped.endswith(":"):  
                    WholeCode += "    " * indentation_level + Line + "\n"  # ვამატებთ შესაბამის ინტენდაციას  
                    indentation_level += 1  # ვზრდით ინტენდაციის დონეს, რადგან ახალი ბლოკი გაიხსნა  

                # თუ ხაზი შეიცავს `return`, `pass`, `break`, ან `continue`, ამ დროს ვამატებთ ერთი დონით ნაკლებ ინტენდაციას
                elif stripped in ["return", "pass", "break", "continue"] or "return" in Line or "break" in Line or "continue" in Line:  
                    WholeCode += "    " * indentation_level + Line + "\n"
                    indentation_level -= 1
                    WholeCode += "\n"  

                # სხვა შემთხვევებში ჩვეულებრივი ინტენდაციით ვამატებთ ხაზს  
                else:  
                    WholeCode += "    " * indentation_level + Line + "\n"  

            # ვასრულებთ WholeCode-ის შესრულებას exec ფუნქციით და ვუთითებთ, რომ გლობალურ სივრცეში უნდა შესრულდეს
            exec(WholeCode, globals()) 

            # Run the dynamically created function with the provided arguments

            inputs = get_test_case_input(json_data, DifficultyDict[difficulty], task_key)

            for i in inputs:
                Answers = Run(func, *i["Input"], expected=i["Output"])
                if not Answers:
                    print("You failed the task")
                    print("You will get 10% of the reward")
                    print("Choose Bank To deposit reward")
                    print("1. GOA BANK")
                    print("2. TBC BANK")
                    print("3. GEO BANK")
                    bank = input("Choose an option: ")
                    while bank not in ["1", "2", "3"]:
                        print("Invalid choice")
                        bank = input("Choose an option: ")
                    if bank == "1":
                        reward = task['Reward'] * 0.1
                        rounded_reward = math.floor(reward * 100) / 100
                        self.Balance["GOA BANK"] += rounded_reward
                        print(f"{task['Reward'] * 0.1} was successfully deposited to GOA BANK.")
                    elif bank == "2":
                        self.Balance["TBC BANK"] += rounded_reward
                        print(f"{task['Reward'] * 0.1} was successfully deposited to TBC BANK.")
                    elif bank == "3":
                        self.Balance["GEO BANK"] += rounded_reward
                        print(f"{task['Reward'] * 0.1} was successfully deposited to GEO BANK.")
                    return
            print("You passed the task")
            print("You will get the reward")
            print("Choose Bank To deposit reward")
            print("1. GOA BANK")
            print("2. TBC BANK")
            print("3. GEO BANK")
            bank = input("Choose an option: ")
            while bank not in ["1", "2", "3"]:
                print("Invalid choice")
                bank = input("Choose an option: ")
            if bank == "1":
                self.Balance["GOA BANK"] += task['Reward']
                print(f"{task['Reward']} was successfully deposited to GOA BANK.")
            elif bank == "2":
                self.Balance["TBC BANK"] += task['Reward']
                print(f"{task['Reward']} was successfully deposited to TBC BANK.")
            elif bank == "3":
                self.Balance["GEO BANK"] += task['Reward']
                print(f"{task['Reward']} was successfully deposited to GEO BANK.")

    def loan(self):

    
        print("So, you want to get a loan from us")
        bank = input("Which bank would you like to get a loan from? ").upper()
        while bank not in self.Balance:
            print("Sorry, we only support GOA, TBC, and GEO banks")
            bank = input("Which bank would you like to get a loan from? ").upper()

        loan_type = input("Would you like a Consumer loan, Car loan, or Business loan? ").lower()
        while loan_type not in ["consumer loan", "car loan", "business loan"]:
            print("Sorry, either we don't support that kind of loan or you misspelled it")
            loan_type = input("Would you like a Consumer loan, Car loan, or Business loan? ").lower()

        if loan_type == "consumer loan":
            print("You have chosen a consumer loan")
            amount = int(input("How much would you like to loan? "))
            while amount > 500000:
                print("We only give loans up to 500,000")
                amount = int(input("How much would you like to loan? "))

            years = int(input("How long would you like to pay the loan? "))
            while years not in range(1, 16):
                print("Sorry, we only give loans for 1-15 years")
                years = int(input("How long would you like to pay the loan? "))

            if years in [1, 2, 3, 4, 5]:
                if amount <= 4500:
                    annual_rate = 0.12  # წლიური განაკვეთი 12%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.09  # წლიური განაკვეთი 9%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.078  # წლიური განაკვეთი 7.8%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.018  # წლიური განაკვეთი 1.8%

            elif years in [6, 7, 8, 9, 10]:
                if amount <= 4500:
                    annual_rate = 0.16  # წლიური განაკვეთი 16%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.10  # წლიური განაკვეთი 10%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.08  # წლიური განაკვეთი 8%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.03  # წლიური განაკვეთი 3%

            elif years in [11, 12, 13, 14, 15]:
                if amount <= 4500:
                    annual_rate = 0.2  # წლიური განაკვეთი 20%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.13  # წლიური განაკვეთი 13%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.10  # წლიური განაკვეთი 10%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.04  # წლიური განაკვეთი 4%

            Total = int(amount * (1 + annual_rate))
            
            print(f"თქვენ გნებავთ {amount} ლარის გატანა {years} წლით. "
                  f"თქვენი წლიური გადასახადი იქნება {int(amount / years * (1 + annual_rate))}. "
                  f"თვიურად მოგიწევთ {int(amount / years * (1 + annual_rate) / 12)}. "
                  f"სულ მოგიწევთ {Total} ლარის გადახდა.")
            
          
            
            self.Loans.append({"Type": loan_type, "amount": Total, "years": years})
            self.Balance[bank] += amount

        elif loan_type == "car loan":
            print("You have chosen a car loan")
            amount = int(input("How much would you like to loan? "))
            while amount > 500000:
                print("We only give car loans up to 500,000")
                amount = int(input("How much would you like to loan? "))

            car_price = int(input("How much does the car cost? "))
            while car_price > amount:
                print("The car price can't be more than the loan amount")
                car_price = int(input("How much does the car cost? "))
            while amount - car_price > 50000:
                print("The difference between the car price and the loan amount can't be more than 50,000")
                car_price = int(input("How much does the car cost? "))

            years = int(input("How long would you like to pay the loan? "))
            while years not in range(1, 16):
                print("Sorry, we only give loans for 1-15 years")
                years = int(input("How long would you like to pay the loan? "))

            if years in [1, 2, 3, 4, 5]:
                if amount <= 4500:
                    annual_rate = 0.20  # წლიური განაკვეთი 20%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.18  # წლიური განაკვეთი 18%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.15  # წლიური განაკვეთი 15%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.12  # წლიური განაკვეთი 12%
                elif 500000 < amount <= 5000000:
                    annual_rate = 0.09  # წლიური განაკვეთი 9%
            elif years in range(6, 11):
                if amount <= 4500:
                    annual_rate = 0.25  # წლიური განაკვეთი 25%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.20  # წლიური განაკვეთი 20%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.18  # წლიური განაკვეთი 18%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.15  # წლიური განაკვეთი 15%
                elif 500000 < amount <= 5000000:
                    annual_rate = 0.12  # წლიური განაკვეთი 12%
            elif years in range(11, 16):
                if amount <= 4500:
                    annual_rate = 0.30  # წლიური განაკვეთი 30%
                elif 4500 < amount <= 10000:
                    annual_rate = 0.25  # წლიური განაკვეთი 25%
                elif 10000 < amount <= 50000:
                    annual_rate = 0.20  # წლიური განაკვეთი 20%
                elif 50000 < amount <= 500000:
                    annual_rate = 0.18  # წლიური განაკვეთი 18%
                elif 500000 < amount <= 5000000:
                    annual_rate = 0.15  # წლიური განაკვეთი 15%

            Total = int(amount * (1 + annual_rate))

            
            print(f"თქვენ გნებავთ {amount} ლარის გატანა {years} წლით. "
                  f"თქვენი წლიური გადასახადი იქნება {int(amount / years * (1 + annual_rate))}. "
                  f"თვიურად მოგიწევთ {int(amount / years * (1 + annual_rate) / 12)}. "
                  f"სულ მოგიწევთ {Total} ლარის გადახდა.")
            
            self.Loans.append({"Type": loan_type, "amount": Total, "years": years})
            self.Balance[bank] += amount

        elif loan_type == "business loan":
            print("You have chosen a business loan")
            amount = int(input("How much would you like to loan? "))
            while amount < 50000000:
                print("We only give business loans from 50,000,000")
                amount = int(input("How much would you like to loan? "))
            while amount > 500000000:
                print("We only give loans up to 500,000,000")
                amount = int(input("How much would you like to loan? "))

            years = int(input("How long would you like to pay the loan? "))
            while years not in range(15, 31):
                print("Sorry, we only give loans for 15-30 years")
                years = int(input("How long would you like to pay the loan? "))

            if years in range(15, 21):
                if amount <= 70000000:
                    annual_rate = 0.40  # წლიური განაკვეთი 40%
                elif 70000000 < amount <= 150000000:
                    annual_rate = 0.32  # წლიური განაკვეთი 32%
                elif 150000000 < amount <= 500000000:
                    annual_rate = 0.25  # წლიური განაკვეთი 25%
                elif 500000000 < amount <= 5000000000:
                    annual_rate = 0.18  # წლიური განაკვეთი 18%
            elif years in range(21, 26):
                if amount <= 70000000:
                    annual_rate = 0.45  # წლიური განაკვეთი 45%
                elif 70000000 < amount <= 150000000:
                    annual_rate = 0.40  # წლიური განაკვეთი 40%
                elif 150000000 < amount <= 500000000:
                    annual_rate = 0.32  # წლიური განაკვეთი 32%
                elif 500000000 < amount <= 5000000000:
                    annual_rate = 0.25  # წლიური განაკვეთი 25%
            elif years in range(26, 31):
                if amount <= 70000000:
                    annual_rate = 0.50  # წლიური განაკვეთი 50%
                elif 70000000 < amount <= 150000000:
                    annual_rate = 0.45  # წლიური განაკვეთი 45%
                elif 150000000 < amount <= 500000000:
                    annual_rate = 0.40  # წლიური განაკვეთი 40%
                elif 500000000 < amount <= 5000000000:
                    annual_rate = 0.32  # წლიური განაკვეთი 32%
            
            Total = int(amount * (1 + annual_rate))

            print(f"თქვენ გნებავთ {amount} ლარის გატანა {years} წლით. "
                  f"თქვენი წლიური გადასახადი იქნება {int(amount / years * (1 + annual_rate))}. "
                  f"თვიურად მოგიწევთ {int(amount / years * (1 + annual_rate) / 12)}. "
                  f"სულ მოგიწევთ {Total} ლარის გადახდა.")
            
            self.Loans.append({"Type": loan_type, "amount": Total, "years": years})
            self.Balance[bank] += amount
           
        print(self.Loans)

    def PayLoan(self):
        print("Which loan woud you like to pay?")
        
        for i in range(len(self.Loans)):
            print(f"{i + 1}.{self.Loans[i]}")
        
        Choice = int(input("Choose Loan To pay off")) - 1

        if self.Loans[Choice]:
            Loan = self.Loans[Choice]
            print("How Much Woud You like to pay off")
            try:
                Amount = int(input("Enter The amount: "))
            except ValueError as e:
                print(e,"Not a valid integer")
            print("1. GOA BANK")
            print("2. TBC BANK")
            print("3. GEO BANK")
            Bank = input("Enter The bank you are going to be paying from: ").upper()

            while Bank not in self.Balance:
                print("Sorry we only support, Goa Bank, Tbc Bank and Geo Bank. Please enter again")
                Bank = input("Enter The bank you are going to be paying from: ").upper()

            while self.Balance[Bank] < Amount:
                print("not enough balance")
                try:
                    Amount = int(input("Enter The amount: "))
                except ValueError as e:
                    print(e,"Not a valid integer")
            
            self.Balance[Bank] -= Amount
            Loan['amount'] -= Amount


