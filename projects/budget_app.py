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
        print(self.ledger)

    def withdraw(self, amount):
        balance = self.get_balance()
        if balance > amount:
            self.ledger.append({"amount": -amount})
            print(self.ledger, "\n")
            return True
        return False
    
    def get_balance(self):
        balance =  0
        for i in self.ledger:
            balance += i["amount"]
        print(f'Balance: {balance}', "\n")
        return balance
    
    def transfer(self, amount, budget_category):
        balance = self.get_balance()
        if balance > amount:
            self.ledger.append({"amount": -amount, "description": f'Transfer to {budget_category.category}'})
            budget_category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
        
