# After you write all your classes, use this file to call them all together and run your program
from classes.budget import Budget


jon_income = {'monthly_income': 14000}
jon_budget_categories = {'budget_categories': ['living', 'food', 'travel', 'savings', 'leisure']}

jon = Budget(jon_income, jon_budget_categories)

#  What would you like to do?
#
#  1. Update Monthly Income
#  2. View Budget Details
#  3. Add Expenses <student_id>
#  4. Remove Expenses
#  5. Exit

menu_prompt = "\nWhat would you like to do?\n\n1. Update Monthly Income\n2. View Budget Details\n3. Add Expenses <student_id>\n4. Remove Expenses\n5. View Budget Details\n5. Exit\n\n"

print("\nWelcome, Jon!")

while True:
    mode = input(menu_prompt)
    if mode == '1':
        jon.update_monthly_income()
    else:
        break
