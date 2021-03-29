# This is the bank account.
# Properties:
#   username, account number(s), bank card(s), balance, credit
# Methods:
#   login, deposit, withdraw, transfer, block_bank_card, check_balance
from Person.person import Person


class Bank(Person):
    pass

    print("This is the", __name__, "class.")

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
        print("The balance of the %s account is" % self.account_number, self.balance)

    # transfer money method
    def transfer(self, number):
        pass
        if self.balance < number:
            print("You do not have enough money to transfer, please deposit some money.")
        elif self.balance >= number:
            self.balance = self.balance - number
            return self.balance
