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
            print(self.ledger)
            return True
        return False
    
    def get_balance(self):
        balance =  0
        for i in self.ledger:
            balance += i["amount"]
        print(f'Balance: {balance}')
        return balance
    
    def transfer(self, amount, budget_category):
        self.ledger.append({"amount": -amount, "description": f'Transfer to {budget_category}'})
        

        
budget = Category("Entertainment")
budget.deposit(300, "TV")
budget.withdraw(100)