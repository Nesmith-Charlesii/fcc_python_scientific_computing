import math

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
        ledger_str += f'{banner}\n'

        expense_sum = 0
        start_balance = 0

        def float_two_spaces(amount):
            # Float the amount first and then change to str data type to use the index method
            float_amount = str(float(amount))
            decimal_index = float_amount.index(".")
            float_amount = float_amount[0:(decimal_index + 3)]

            # Check that all amounts end with 2 digits
            split_decimal = float_amount.split(".")
            if len(split_decimal[1]) < 2:
                split_decimal[1] = split_decimal[1] + "0"
                float_amount = ".".join(split_decimal)

            return float_amount

        for i in self.ledger:
            description = ""
            
            if len(i["description"]) > 23:
                description += i["description"][0:23]
            else: description += i["description"]
            
            float_amount = float_two_spaces(i["amount"])

            if float(float_amount) > -1:
                start_balance += float(float_amount)
            elif float(float_amount) < 0:
                expense_sum += float(float_amount)

            desc_length = len(description)
            right_align = 30 - desc_length

            ledger_str += f'{description}{float_amount:>{right_align}}\n'
            # ACCOUNT FOR TRANSACTION GREATER THAN 7 DIGITS

        total = start_balance + expense_sum
        ledger_str += f'Total: {total}'

        return ledger_str

    def deposit(self, amount, description=""):
        deposit_obj = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(deposit_obj)
        #print(f'{self.category} ledger: {self.ledger}')

    def withdraw(self, amount, description=""):
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


def create_spend_chart(categories):

    category_index = (len(categories) - 1)
    category_list = []
    
    def calculate_percentage(category_index):
        if category_index < 0:
            return category_list
        else:
            category = categories[category_index].category
            expense_sum = 0

            for i in categories[category_index].ledger:
                if i["amount"] < 0:
                    expense_sum += abs(i["amount"])
            category_list.append({"category":category, "amount": expense_sum})

            if category_index == 0:
                key_to_sum = "amount"
                total_spent = sum(i[key_to_sum] for i in category_list)

                for i in category_list:
                    percent = (i["amount"] * 100) / total_spent
                    if percent < 10:
                        percent = 0
                    i["percentage"] = round(percent, -1)
            return calculate_percentage(category_index - 1)
        
    calculate_percentage(category_index)
    
    chart = f'Percentage spent by category\n'
    dashes = ""
    print(category_list)
    for i in range(100,-1,-10):
        chart += f'{i:>{3}}| '
        for cat in category_list:
            percentage = cat["percentage"]
            if percentage >= i:
                chart += f'o  '
        chart += "\n"
    
    # For each category, there are 3 dashes
    # Add one additional dash for the spacing between first bar of chart and y-axis
    dashes += "---" * (len(category_list)) + "-"
    chart += f'{dashes:>{len(dashes) + 4}}\n'

    max_letter_count = 0
    for c in categories:
        if len(c.category) > max_letter_count:
            max_letter_count = len(c.category)
    
    line_letters = ""
    for k in range(0, max_letter_count):
        for item in category_list:
            if len(item["category"]) > k:
                letter = item["category"][k]
                line_letters += f'{letter}  '
            else:
                line_letters += "   "
        chart += f'     {line_letters}\n'
        line_letters = ""
    print(chart)
    return chart


# food = Category("Food")
# clothing = Category("Clothing")
# entertaiment = Category("Entertainment")
# well_being = Category("Well Being")

# food.deposit(1000, "initial deposit")
# food.withdraw(220.15, "groceries")
# food.withdraw(15.898434, "restaurant and more food")
# food.withdraw(20, "starbucks")
# food.withdraw(32, "thaiphoon bistro")
# food.withdraw(30, "rock n' roll sushi")
# food.withdraw(70, "Cowfish Sushi Bar")
# food.withdraw(65, "Crafty Crab")
# food.transfer(50, clothing)

# clothing.deposit(600, "initial deposit")
# clothing.withdraw(80.15, "sunday best")
# clothing.withdraw(55.00, "atheltic shoes")
# clothing.withdraw(120.00, "casual wear")

# entertaiment.deposit(1200, "initial deposit")
# entertaiment.withdraw(220.15, "tv")
# entertaiment.withdraw(15.89, "aux cable")
# entertaiment.withdraw(20, "phone charger")
# entertaiment.withdraw(12, "remote control")
# entertaiment.withdraw(60, "led lights")
# entertaiment.withdraw(120, "computer monitor")
# entertaiment.withdraw(199, "bose speakers")
# entertaiment.transfer(200, food)

# well_being.deposit(800, "initial deposit")
# well_being.withdraw(200.15, "Spa")
# well_being.withdraw(50, "self-help book")
# well_being.withdraw(40, "massage")
# well_being.withdraw(60, "boxing pt")
# well_being.withdraw(120, "vacation")
# well_being.withdraw(140, "therapy")
# well_being.transfer(200, clothing)

#print(food, "\n")
# print(clothing)
# print(entertaiment)
# print(well_being)

#create_spend_chart([food, clothing, entertaiment, well_being])

food = Category("Food")
entertainment= Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
print("\n")
create_spend_chart([business, food, entertainment])