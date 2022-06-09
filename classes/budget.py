# from budgetcategory import BudgetCategory
import csv

class Budget:
    def __init__(self):
        self.monthly_income = 0
        self.budget_categories = []
        self.get_initial_budget_categories()
        self.get_initial_monthly_income()
        
    # def add_budget_category(self):
    #     with open('data/budgetdetails.csv', 'w', newline='') as csv_file:
    #         fieldnames = self.budget_categories
    #         csv_data = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         csv_data.writeheader()
    
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
        
    def load_data(self):
        
        pass    
        
    def get_initial_budget_categories(self):
        get_categories = input("\nLet's get started.\n\nPlease list which categories you would like to include in your budget:\n(Example: Living, Food, Travel)\n\n> ")
        list = get_categories.split(',')
        for category in list:
            self.budget_categories.append(category.strip().lower())
            
    def add_budget_category(self):
        new_category = input("\nPlease input a new category title:\n\n> ")
        self.budget_categories.append(new_category.strip().lower())
    
    def get_initial_monthly_income(self):
        get_monthly_income = input("\nNext, please input your monthly income:\n\n> ")
        income_string = ''
        for elem in get_monthly_income:
            if '0123456789'.find(elem) > -1:
                income_string += elem;
        self.monthly_income = int(income_string)
        
    def update_monthly_income(self):
        new_amount = input("Please enter your new monthly income in dollars:  $")
        previous_amount = self.monthly_income
        self.monthly_income = new_amount
        print(f"\nYour monthly income has been updated from ${previous_amount} to ${self.monthly_income}")        
        
    def save_monthly_income(self):
        with open('data/monthlyincome.csv', 'w', newline='') as csv_file:
            fieldnames = "monthly_income"
            csv_reader = csv.DictReader(csv_file)
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
        
        
        
        
# 'living': 8000
# 'food': 1000
# 'travel': 1000
# 'savings': 2000
# 'leisure': 2000