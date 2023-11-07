# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
#from unittes

food = budget.Category("Food")
#print(food.name)
#print(food.ledger)
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.ledger)
#print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
#print(food.ledger)
#print(clothing.ledger)
clothing.withdraw(25.55)
clothing.withdraw(100)
#print(food.ledger)
#print(clothing.ledger)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
#print(auto.ledger)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))

food = budget.Category("Food")
food.deposit(900, "deposit")
food.deposit(45.56)
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.deposit(900, "deposit")
good_withdraw = food.withdraw(45.67)
print(food)
print(good_withdraw)

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food)
transfer_amount = 20
food.get_balance()
entertainment.get_balance()
food.transfer(transfer_amount, entertainment)
food.get_balance()
entertainment.get_balance()
print(food)
print(entertainment)

food = budget.Category("Food")
food.deposit(10, "deposit")
print(food.check_funds(20))
print(food.check_funds(10))

food = budget.Category("Food")
food.deposit(100, "deposit")
print(food.withdraw(100.10))

food = budget.Category("Food")
food.deposit(100, "deposit")
print(food.transfer(200, entertainment))

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print(food)

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))