from user import User
class Admin:
    def __init__(self):
        self.users = []
        self.total_loans = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        print(f"Account created successfully! Account Number: {user.account_number}")

    def delete_account(self, account_number):
        user = next((u for u in self.users if u.account_number == account_number), None)
        if user:
            self.users.remove(user)
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Error: Account not found.")

    def show_all_users(self):
        if self.users:
            print("List of User Accounts:")
            for user in self.users:
                print(f"Name: {user.name}, Account Number: {user.account_number}, Balance: {user.balance}")
        else:
            print("No users found.")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total available balance in the bank: {total_balance}")

    def check_total_loan(self):
        print(f"Total loan amount: {self.total_loans}")

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        status = "enabled" if self.loan_feature else "disabled"
        print(f"Loan feature has been {status}.")
