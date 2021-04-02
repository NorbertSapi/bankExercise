# This is a Person class

class Person:
    pass
    print("This is a message from the %s class." % __name__)

    def __init__(self, first_name, second_name, account_number, mobile):
        self.first_name = first_name
        self.second_name = second_name
        self.account_number = account_number
        self.mobile = mobile
