'''
You are required to build a Personal Budget management application. The application will manage budget categories like food, entertainment, utilities, etc. ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class - Create a class 'Budget Category' with private attributes for category name and allocated budget. Initialize these attributes in the constructor.

Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. Ensure that the setter methods include validation (e.g., budget should be a positive number).

Task 3: Add Budget Functionality - Implement a method to add expenses to a catgetoy and adjust the budget accordingly. Validate the expense amount before making deductions from the budget.

Task 4: Display Budget Details - Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

'''
budget = {}

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self, new_category):
        self.__category_name = new_category

    def set_allocated_budget(self, new_budget):
        self.__allocated_budget = new_budget
    

    def add_expense(self, amount):
        if 0 < amount <= self.get_allocated_budget():
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            print(f"Expense of {amount} added.")
        else:
            print("Invalid expense amount.")

    def display_category_summary(self):
        print(f"This is the {self.get_category_name()} category. This is the current budget: {self.get_allocated_budget()}")
        # if category in # No idea for the rest of this part, do I need a list or dictionary perhaps?


food_category = BudgetCategory("Food", 500)
# food_category.display_category_summary()
# food_category.add_expense(100) 
# food_category.display_category_summary()

shopping_category = BudgetCategory("Shopping", 200)

budget["Food"] = food_category
budget["Shopping"] = shopping_category



# while True:
#     print("Welcome to your budget calculator. Define the budget you want to check!")
#     for category in budget:
#         print(category)
    
#     category_selection = input("Please select the category here: ")

#     option_selection = int(input("Would you like to 1. Add an expense? 2. Get category name. 3. Get summary?"))

#     if option_selection == 1:
#         expense_amount = int(input("How much would you like to add as an expense? "))
#         budget[category_selection.title()].add_expense(expense_amount)
#         print(f"Your expense of {expense_amount} has been deducted from your {budget[category_selection.title()].get_category_name()} budget")
#     elif option_selection == 3:
#         budget[category_selection.title()].display_category_summary()
