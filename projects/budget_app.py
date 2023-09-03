class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        #print(f'{self.category} budget instantiated')

    def __str__(self):
        # To split individual characters, use 'list' instead of split method
        category = self.category
        split_category = list(category)
        ledger_str = ""

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
            right_align = 30 - desc_length

            ledger_str += f'{description}{amount:>{right_align}}\n'
            # ACCOUNT FOR TRANSACTION GREATER THAN 7 DIGITS
        return ledger_str

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


# def create_spend_chart(categories):

#     chart_title = "Percentage spent by category"
#     print(categories)
#     category_index = (len(categories) - 1)
#     expense_percentage = {}
    
#     def percent_spent(category_index):
#         if category_index == 0:
#             return "recursion complete"
#         else:
#             pass
            # print(categories[category_index])
            # category_name = categories[category_index].category
            # expense_sum = 0

            # for i in categories[category_index]:
            #     print(i)
                # if i["amount"] < 0:
                #     print(i["amount"])
                #     expense_sum += i["amount"]
            # print(f'{chart_title}\n{expense_sum}')
            # return percent_spent(category_index - 1)
        
    # percent_spent(category_index)

    
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.898434, "restaurant and more food")
food.transfer(50, clothing)

print(food)
#create_spend_chart([food, clothing])