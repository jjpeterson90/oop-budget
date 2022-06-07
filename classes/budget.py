# from budgetcategory import BudgetCategory
import csv

class Budget:
    def __init__(self, monthly_income, budget_categories):
        self.monthly_budget = monthly_income
        self.budget_categories = list(budget_categories.values())[0]
        
        # initialize CSV file with requested budget categories as header
        # Can use 'x' mode to create a new file and open it for writing *********
        with open('data/budgetdetails.csv', 'w', newline='') as csv_file:
            fieldnames = self.budget_categories
            csv_data = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_data.writeheader()
       
    def update_monthly_income(self):
        new_amount = input("Please enter your new monthly income in dollars:  $")
        previous_amount = self.monthly_income
        self.monthly_income = new_amount
        print(f"Your monthly income has been updated from ${previous_amount} to ${self.monthly_income}")
    
    def add_budget_category(self):
        pass
    
    def remove_budget_category(self):
        pass
    
    def calculate_budget(self):
        pass
    
    def calculate_new_expenses(self):
        pass
    
    def add_expense(self):
        pass
    
    def remove_expense(self):
        pass
    
    
    
        
# 'living': 8000
# 'food': 1000
# 'travel': 1000
# 'savings': 2000
# 'leisure': 2000