# This is the bank account.
# Properties:
#   username, account number(s), bank card(s), balance, credit
# Methods:
#   login, deposit, withdraw, transfer, block_card, get_balance
from Person.person import Person


# get_help
def get_help():
    issue = input("Do you have any issue?")
    if issue is "Yes":
        print("Please call the helpline: 07827362.")
    else:
        print("Thanks for your feedback.")


class Bank(Person):
    pass

    print("This is a message from the %s class." % __name__)

    def __init__(self, first_name, second_name, account_number, mobile, sort_code, bank_card, balance):
        super().__init__(first_name, second_name, account_number, mobile)
        self.sort_code = sort_code
        self.bank_card = bank_card
        self.balance = balance

    # get user_name method
    def get_user_name(self):
        return "%s %s" % (self.first_name, self.second_name)

    # login
    def login(self):
        return "Welcome %s, you have signed in." % Bank.get_user_name(self)

    # get balance method
    def get_balance(self):
        return "The balance of the %s account is" % self.account_number,  self.balance

    # transfer money method
    def transfer(self, amount):
        if self.balance < amount:
            print("You do not have enough money to transfer, please deposit some money.")
        elif self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance

    # block a bank card
    def block_card(self):
        return "Your bank card: card number %s is blocked." % self.bank_card

    # make a deposit account
    def make_deposit(self, amount):
        print("Would you like to deposit %s pounds to your account?" % amount)
        self.balance += amount
        return self.get_balance()

    # withdraw money
    def withdraw_money(self, amount):
        print("Would you like to withdraw %s pounds from your account?" % amount)
        self.balance -= amount
        return self.get_balance()
