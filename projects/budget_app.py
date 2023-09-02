class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        #print(f'{self.category} budget instantiated')

    def deposit(self, amount, description=""):
        deposit_obj = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(deposit_obj)
        #print(f'{self.category} ledger: {self.ledger}')

    def withdraw(self, amount, description):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -amount, "description": description})
            #print(self.ledger)
            return True
        return False
    
    def get_balance(self):
        balance =  0
        for i in self.ledger:
            balance += i["amount"]
        #print(f'{self.category} balance: {balance}')
        return balance
    
    def transfer(self, amount, budget_category):
        funds = self.check_funds(amount)
        if funds:

            self.ledger.append({"amount": -amount, "description": f'Transfer to {budget_category.category}'})
            #print(f'Transfer to {budget_category.category}')

            budget_category.deposit(amount, f'Transfer from {self.category}')
            #print(f'Transfer from {self.category}')

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
        
        banner = "".join(split_category)
        print(banner)

        for i in self.ledger:
            description = ""
            amount = None
            if len(i["description"]) > 23:
                description += i["description"][0:23]
            else: description += i["description"]
            
            # Float the amount first and then change to str data type to use the index method
            amount = str(float(i["amount"]))
            decimal_index = amount.index(".")
            amount = amount[0:(decimal_index + 3)]

            # Check that all amounts end with 2 digits
            split_decimal = amount.split(".")
            if len(split_decimal[1]) < 2:
                split_decimal[1] = split_decimal[1] + "0"
                amount = ".".join(split_decimal)

            desc_length = len(description)
            amount_length = len(amount)
            right_align = 30 - desc_length

            print(f'{description}{amount:>{right_align}}')
            
            
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.898434, "restaurant and more food")
food.transfer(50, clothing)

food.display_budget()