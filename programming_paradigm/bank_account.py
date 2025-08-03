class BankAccount:
    def __init__(self, initial_balance=0):

        self._account_balance = initial_balance

    def deposit(self, amount):

        if isinstance(amount, (int, float)) and amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount. Must be a positive number.")

    def withdraw(self, amount):

        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid withdrawal amount. Must be a positive number.")
            return False

        if amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):

        print(f"Current Balance: ${self._account_balance:.2f}")
