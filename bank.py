# This is the bank account.
# Properties:
#   username, account number(s), bank card(s), balance, credit
# Methods:
#   login, deposit, withdraw, transfer, block_bank_card, check_balance


class Bank:
    pass

    print("This is the", __name__, "class.")

    def __init__(self, first_name, second_name, account_number, sort_code, bank_card, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.account_number = account_number
        self.sort_code = sort_code
        self.bank_card = bank_card
        self.balance = balance

# get user_name method
    def get_user_name(self):
        return self.first_name + " " + self.second_name

# get balance method
    def get_balance(self):
        print("The balance of the", self.account_number, "account is", self.balance)

# transfer money method
    def transfer(self, number):
        pass
        if self.balance < number:
            print("You do not have enough money to transfer, please deposit some money.")
