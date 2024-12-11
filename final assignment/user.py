class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.name + self.email
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposit successful! New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrawal successful! New balance: {self.balance}")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def show_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def take_loan(self, amount, loan_feature):
        if not loan_feature:
            print("Loan feature is currently disabled.")
            return
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan taken: {amount}")
            print(f"Loan approved! New balance: {self.balance}")
        else:
            print("Error: Maximum loan limit reached.")

    def transfer(self, amount, recipient):
        if self.balance < amount:
            print("Error: Insufficient balance.")
        elif not isinstance(recipient, User):
            print("Error: Account does not exist.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received {amount} from {self.name}")
            print(f"Transfer successful! New balance: {self.balance}")
