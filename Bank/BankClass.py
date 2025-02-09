
# შექმენი კლასი/ტიპი როგორც int str bool და float.
# მიანიშნე მას თავისი ფუნქციები
class Bank():
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = {
            "GOABank": 0.0,
            "TBCBank": 0.0,
            "BankOfGeorgia": 0.0,
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
    
    def Deposit(self,Amount : float,Bank:str):
        self.Balance[Bank] += Amount

    def Withdraw(self,Amount: float,Bank:str):
        self.Balance[Bank] += Amount