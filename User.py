"""make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150

BONUS: transfer_money(self, other_user, amount) 
- have this method decrease the user's balance by the amount and add that amount to other other_user's balance"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        #print the users name and account balance
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        #decrease the users balance, add the amount taken out to another users acct
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        
mars = User("mars", "sentfrom-mars@planet.com")
mars.make_deposit(10000)
mars.make_deposit(22300)
mars.make_deposit(722)
mars.make_withdrawal(722)
mars.display_user_balance()
creed = User("creed", "creed-aim-high@prosper.com")
creed.make_deposit(5000)
creed.make_deposit(15000)
creed.make_withdrawal(2300)
creed.make_withdrawal(573)
creed.display_user_balance()
brooklyn = User("brooklyn", "hyped_doggie24-7@alwaysonten.com")
brooklyn.make_deposit(6479)
brooklyn.make_withdrawal(360)
brooklyn.make_withdrawal(100)
brooklyn.make_withdrawal(50)
brooklyn.display_user_balance()
#transfer money
mars.transfer_money(brooklyn, 2300)
mars.display_user_balance()
brooklyn.display_user_balance()
        