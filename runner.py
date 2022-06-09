# After you write all your classes, use this file to call them all together and run your program
from classes.budget import Budget

#jon_budget_categories = {'budget_categories': ['living', 'food', 'travel', 'savings', 'leisure']}

#  What would you like to do?
#
#  1. Add Expense
#  2. Update Monthly Income
#  3. View Budget Details
#       1. Budget Breakdown
#       2. Current Monthly Income
#       3. My Monthly Costs
#  4. Exit

MAIN_MENU = "\nWhat would you like to do?\n\n" \
            "1. Add Expense\n" \
            "2. Update Monthly Income\n" \
            "3. View Budget Details\n" \
            "4. Exit\n\n"
            
BUDGET_DETAILS_OPTIONS = "\nSelect one:\n1. Budget Breakdown\n2. Current Monthly Income\n3. My Monthly Costs\n"

print("\nWelcome, Jon!")

jon = Budget()

while True:
    mode = input(MAIN_MENU)
    if mode == '1':
        pass # Add Expense
    if mode == '2':
        jon.update_monthly_income()
    if mode == '3':
        mode3 = input(BUDGET_DETAILS_OPTIONS)
        if mode3 == '1':
            pass
        if mode3 == '2':
            pass
        if mode3 == '3':
            pass
    if mode == '4':
        print("\nGoodbye\n\n")
        break
