""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest, interest_earned=0):
        self.balance = balance
        self.interest = interest
        self.interest_earned = interest_earned

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    def get_balance(self):
        """Gets the balance for the account"""
        return self.balance


    def calculate_interest(self, months):
        """Calculates the interest gained for the account"""
        monthly_rate = self.interest / 12
        interest_earned = self.balance *(monthly_rate/100 ) * months
        return interest_earned