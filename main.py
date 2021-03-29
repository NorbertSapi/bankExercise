# This is a exercise to practice Objects. The exercise simulates a bank application.
from bank import Bank

# initialize the object
user1 = Bank("John", "Smith", 12345678, 654321, 321456789, 0)

user_name1 = Bank.get_user_name(user1)
print(user_name1)
Bank.get_balance(user1)
