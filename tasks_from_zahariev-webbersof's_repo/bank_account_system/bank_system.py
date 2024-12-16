# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = {}  # List to store corresponding balances
transaction_histories = {}  # List to store transaction histories
loans = {}  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    user = input("Enter account name: ")
    # 2. Add the new account holder to the list of account holders.
    account_holders.append(user)
    # 3. Initialize the balance to 0 for the new account.
    balances[user] = [0.00]
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories[user] = []
    # 5. Initialize the outstanding loan amount to 0.
    loans[user] = [0.00]
    # 6. Notify the user of the successful account creation.
    print("Your account was successfully created.")


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    user = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if user in account_holders:
    # 3. If the account exists, prompt the user for the amount to deposit.
        amount_to_deposit = float(input("Enter amount for deposit: "))
    # 4. Update the account's balance with the deposited amount.
        balances[user].append(balances[user][-1] + amount_to_deposit)
    # 5. Log the transaction in the account's transaction history.
        transaction_histories[user].append(amount_to_deposit)
    # 6. Display the updated balance to the user.
        print("Your account balance is:", balances[user][-1])
    # 7. If the account does not exist, inform the user.
    else:
        print("This account is not existing")


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    user = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if user in account_holders:
    # 3. If the account exists, prompt the user for the amount to withdraw.
        amount_to_withdraw = float(input("Enter amount to withdraw: "))
        # 4. Check if there are sufficient funds for the withdrawal.
        if amount_to_withdraw <= balances[user][-1]:
        # 5. If funds are sufficient, update the balance and log the transaction.
            balances[user].append(balances[user][-1] - amount_to_withdraw)
            transaction_histories[user].append(-amount_to_withdraw)
        # 6. Display the updated balance to the user.
            print("Your account balance is:", balances[user][-1])
        # 7. If insufficient funds, inform the user.
        else:
            print("Insufficient funds.")

    # 8. If the account does not exist, inform the user.
    else:
        print("This account is not existing")


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    user = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if user in account_holders:
    # 3. If the account exists, display the current balance.
        print("Your account balance is:", balances[user][-1])

    # 4. If the account does not exist, inform the user.
    else:
        print("This account is not existing")


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if account_holders:
    # 2. If there are accounts, loop through each account holder.
        for user in account_holders:
    # 3. Display the account holder's name, balance, and outstanding loan amount.
            user_name = user
            user_balance = balances[user][-1]
            user_loans = loans[user][-1]
            print(f"{user_name} has account balance: {user_balance} leva and loans amount: {user_loans} leva")
    # 4. If there are no accounts, inform the user.
    else:
        print("No accounts found")


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender = input("Enter sender account name: ")
    receiver = input("Enter receiver account name: ")
    # 2. Check if both accounts exist in the system.
    if sender in account_holders and receiver in account_holders:
    # 3. If both accounts exist, prompt the user for the amount to transfer.
        amount_to_transfer = float(input("Enter amount to transfer: "))
    # 4. Check if the sender has sufficient funds for the transfer.
        if amount_to_transfer <= balances[sender][-1]:
    # 5. If funds are sufficient, update both balances and log the transactions.
            balances[sender].append(balances[sender][-1] - amount_to_transfer)
            balances[receiver].append(balances[receiver][-1] + amount_to_transfer)

            transaction_histories[sender].append(-amount_to_transfer)
            transaction_histories[receiver].append(amount_to_transfer)
    # 6. Inform the user of the successful transfer.
            print("Amount was transferred.")
    # 7. If insufficient funds or if either account does not exist, inform the user.
        else:
            print("Insufficient funds.")


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    user = input("Enter your account name: ")
    # 2. Check if the account exists in the system.
    if user in account_holders:
    # 3. If the account exists, display the transaction history.
        if transaction_histories[user]:
            for transaction in transaction_histories[user]:
                if transaction > 0:
                    print(f" Deposit: {transaction} leva")

                else:
                    print(f" Withdraw: {transaction} leva")
    # 4. If there are no transactions, inform the user.
        else:
            print("No transactions for this account")
    # 5. If the account does not exist, inform the user.
    else:
        print("This account is not existing")


def apply_for_loan():
    """Apply for a loan."""
    user = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if user in account_holders:
        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[user].append(balances[user][-1] + loan_amount)
            loans[user].append(loan_amount * (1 + INTEREST_RATE)) # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {user}. New balance: {balances[user][-1]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    user = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if user in account_holders:

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[user][-1]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[user][-1]:
            # Update balance and outstanding loan amount
            balances[user][-1] -= repayment_amount
            loans[user][-1] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {user}. Remaining loan: {loans[user][-1]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Total funds")
    print("11. Delete Account")
    print("12. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def display_total_funds():
    total_funds = 0
    # Check for existing users
    if account_holders:
        for user in account_holders:
    # Sum the last balances of all users
            total_funds += balances[user][-1]
        print(f"Total funds: {total_funds:.2f} leva")
    else:
        print("No accounts found")


def delete_account():
    user = input("Enter account name: ")
    # Check for existing user
    if user in account_holders:
        account_holders.remove(user)
        del balances[user]
        del transaction_histories[user]
        del loans[user]

    else:
        print("This account is not existing")


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            display_total_funds()
        elif choice == 11:
            delete_account()
        elif choice == 12:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()