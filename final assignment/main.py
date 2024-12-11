from admin import Admin
admin = Admin()
while True:
    print("\n=== Bank Management System ===")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("\n=== Admin Menu ===")
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. Show All Users")
            print("4. Check Total Bank Balance")
            print("5. Check Total Loan Amount")
            print("6. Lone ON OFF")
            print("7. Logout")
            admin_choice = input("Enter your choice: ")
            if admin_choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                account_type = input("Enter account type (Savings/Current): ")
                admin.create_account(name, email, address, account_type)
            elif admin_choice == "2":
                account_number = input("Enter account number to delete: ")
                admin.delete_account(account_number)

            elif admin_choice == "3":
                admin.show_all_users()

            elif admin_choice == "4":
                admin.check_total_balance()

            elif admin_choice == "5":
                admin.check_total_loan()

            elif admin_choice == "6":
                admin.toggle_loan_feature()

            elif admin_choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        account_number = input("Enter your account number: ")
        user = next((u for u in admin.users if u.account_number == account_number), None)
        if not user:
            print("Error: Account not found.")
            continue

        while True:
            print("\n=== User Menu ===")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Show Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Logout")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)

            elif user_choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)

            elif user_choice == "3":
                user.check_balance()

            elif user_choice == "4":
                user.show_transaction_history()

            elif user_choice == "5":
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount, admin.loan_feature)

            elif user_choice == "6":
                recipient_account = input("Enter recipient account number: ")
                recipient = next((u for u in admin.users if u.account_number == recipient_account), None)
                amount = float(input("Enter amount to transfer: "))
                user.transfer(amount, recipient)

            elif user_choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        print("Thank you for using the Bank Management System!")
        break
    else:
        print("Invalid choice. Please try again.")