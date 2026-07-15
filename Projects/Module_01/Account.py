
# Addis Bank - Account Management System

class Account:
    def __init__(self, owner, account_number, balance=1500):
        # Public attributes
        self.owner = owner
        self.account_number = account_number

        # Private attribute
        self.__balance = balance

    # Read-only property
    @property
    def balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0 ETB.")
        else:
            self.__balance += amount
            print(f"{amount:.2f} ETB deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0 ETB.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount:.2f} ETB withdrawn successfully.")

    # Display account statement
    def statement(self):
        print("\n========== Account Statement ==========")
        print(f"Owner          : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.balance:.2f} ETB")
        print("=======================================\n")


# ==========================================
# Main Program
# ==========================================

account1 = Account("Abebe Kebede", "10010001")

account1.statement()

print("Depositing 5000 ETB...")
account1.deposit(5000)

print("Withdrawing 1500 ETB...")
account1.withdraw(1500)

print("Trying to withdraw 10000 ETB...")
account1.withdraw(10000)

print("Trying to deposit -500 ETB...")
account1.deposit(-500)

account1.statement()