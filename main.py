# This is a exercise to practice Objects. The exercise simulates a bank application.
from bank import Bank

# initialize the object
user1 = Bank("John", "Smith", "12345678", "07746417399", "654321", "321456789", 200)

user_name1 = Bank.get_user_name(user1)
print(user_name1)
print(Bank.login(user1))
Bank.get_balance(user1)
print("'You make a 50 pounds transfer.'")
print("The balance of the %s is" % user1.account_number, Bank.transfer(user1, 50))
print(Bank.block_card(user1))
print(Bank.make_deposit(user1, 300))
print(Bank.withdraw_money(user1, 120))

if __name__ == "__main__":
    print("This is main: %s." % __name__)
