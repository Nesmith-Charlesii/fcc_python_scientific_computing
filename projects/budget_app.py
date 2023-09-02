class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        print(f'{self.category} budget instantiated')

    def deposit(self, amount, description=""):
        deposit_obj = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(deposit_obj)
        print(f'{self.category} ledger: {self.ledger}', "\n")

    def withdraw(self, amount):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -amount})
            print(self.ledger, "\n")
            return True
        return False
    
    def get_balance(self):
        balance =  0
        for i in self.ledger:
            balance += i["amount"]
        print(f'{self.category} balance: {balance}', "\n")
        return balance
    
    def transfer(self, amount, budget_category):
        funds = self.check_funds(amount)
        if funds:

            self.ledger.append({"amount": -amount, "description": f'Transfer to {budget_category.category}'})
            print(f'Transfer to {budget_category.category}')

            budget_category.deposit(amount, f'Transfer from {self.category}')
            print(f'Transfer from {self.category}', "\n")

            return True
        return False
    
    def check_funds(self, amount):
        balance = self.get_balance()
        if balance < amount:
            return False
        return True

        
entertainment = Category("entertainment")
entertainment.deposit(500, "entertainment system")

clothing = Category("clothing")
clothing.deposit(300, "casual wear")

entertainment.transfer(200, clothing)
entertainment.get_balance()
clothing.get_balance()