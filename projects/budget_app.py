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

    def display_budget(self):
        # To split individual characters, use 'list' instead of split method
        category = self.category
        split_category = list(category)

        while len(split_category) < 30:
            split_category.append("*")
            split_category.insert(0, "*")

        banner = " ".join(split_category)
        print(banner)


food = Category("food")
food.display_budget()