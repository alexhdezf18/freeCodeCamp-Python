class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            
            category.deposit(amount, f"Transfer from {self.name}")
            
            return True
        
        return False
    
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23].ljust(23)}"
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
            
        output = title + items + "Total: " + str(self.get_balance())
        return output

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)

    percentages = []
    for amount in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            percent = (amount / total_spent) * 100
            percentages.append(int(percent // 10) * 10)

    header = "Percentage spent by category\n"
    chart = ""
    
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        
        for percent in percentages:
            if percent >= i:
                chart += "o  " 
            else:
                chart += "   " 
        chart += "\n"
        
    dash_width = len(categories) * 3 + 1
    footer = "    " + "-" * dash_width + "\n"
    
    names = [cat.name for cat in categories]
    max_length = max([len(n) for n in names])
    names_str = ""
    
    for i in range(max_length):
        names_str += "     " 
        for name in names:
            if i < len(name):
                names_str += name[i] + "  "
            else:
                names_str += "   "
        
        if i < max_length - 1:
            names_str += "\n"
            
    return header + chart + footer + names_str

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))