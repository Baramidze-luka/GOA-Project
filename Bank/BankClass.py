

class Bank():
    # ბანკის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Bank() ფუნქციას გამოიყენებ
    def __init__(self):
        self.Balance = 0.0

    # self აღნიშნავს თავის თავს ანუ ბანკს

    # Amount : float არის type check რომელიც გადააქცევს მოცემულ არგუმენტს იმ ტიპად რასაც აძლევ
    # -> bool: აღნიშნავს რომ ფუნქცია დააბრუნებს boolean ტიპს

    def Deposit(self,Amount : float) -> bool:
        pass

    def Withdraw(self,Amount: float) -> bool:
        pass