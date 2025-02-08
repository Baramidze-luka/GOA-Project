
# შექმენი კლასი/ტიპი როგორც int str bool და float.
# მიანიშნე მას თავისი ფუნქციები
class Bank():
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = 0.0

    # self აღნიშნავს თავის თავს ანუ ბანკს

    # Amount : float არის type check რომელიც გადააქცევს მოცემულ არგუმენტს იმ ტიპად რასაც აძლევ
    # () -> bool: აღნიშნავს რომ ფუნქცია დააბრუნებს boolean ტიპს

    # ფუნქცია აბრუნებს როცა მასში არის გამოყენებული return

    # def Deposit(self,Amount : float) -> bool:
    #     return True

    # Answer = Deposit() რომელიც მომცემს True'ს
    # როგორც Input = input() გვაძლევს სტრინგს ეს არის პასუხი return ის გამოყენებით
    
    def Deposit(self,Amount : float):
        pass

    def Withdraw(self,Amount: float):
        pass