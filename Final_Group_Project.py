import json
import argparse
from datetime import datetime

class User(Exception):
    pass

    def authenticate_user(self, username, password):
        """
        Claim: Abrar
        Technique: With statement. Conditional expression
        
        Authenticates the user by comparing provided info with the stored info

        Parameters:
        
        username (str): The username entered by the user.
        password (str): The password entered by the user.

        Returns:

        bool: True if authentication is good, false otherwise
        
        """
        with open(self.user_data_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['username'] == username and self.verify_password(password, row['hashed_password']):
                    return True

        return False

    def hash_password(self, password):
        """
        Hashes the password provided

        Parameters:
        password (str): The password given

        Returns:
        str: The hashed password 
        
        """
        password_bytes = password.encode('utf-8')
        hash_obj = hashlib.sha256(password_bytes)
        return hash_obj.hexdigest()

    def verify_password(self, input_password, stored_hash):
        """
        Verifies if the given password matches the stored and hashed password

        Parameters:
        input_password(str): The password entered by the user
        stored_hash (str): The hashed and stored password

        Returns: 
        bool: True if a match, False otherwise
        
        """
        hashed_input = self.hash_password(input_password)
        return hashed_input == stored_hash

    def login(self):
        """
        The Login screen. Prompts the user to enter their credentials.
        Displays account options after logging in.

        Raises:
        UserError: If the entered credential are invalid 

        
        """
        print("Log in to your account:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.authenticate_user(username, password):
            print("Login successful!")
            self.logged_in_user = username
            self.show_account_options()
        else:
            raise UserError("Invalid username or password")





class UserAccount:
    def __init__(self):
        self.transaction_history = []  # Initialize transaction history

    def add_transaction(self, transaction_type, amount):
        '''
        This functions adds transactions made by the user into their account
        organized by the date stamp. 

        Parameters: transaction_type
        '''
        timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        new_transaction = pd.DataFrame({
            "Type": [transaction_type],
            "Amount": [amount],
            "Timestamp": [timestamp]
        })

        self.transaction_history = pd.concat([self.transaction_history, new_transaction], ignore_index=True, sort=False)

def main():
    parser = argparse.ArgumentParser(description="User Account Transactions")
    parser.add_argument("--type", choices=["deposit", "withdrawal"], required=True, help="Transaction type: 'deposit' or 'withdrawal'")
    parser.add_argument("--amount", type=float, required=True, help="Transaction amount")
    parser.add_argument("--timestamp", default=datetime.now().strftime("%m-%d-%Y %H:%M:%S "), help="Transaction timestamp")
    parser.add_argument("--source-account", help="Source account for the transaction")

    args = parser.parse_args()

    user_account = UserAccount()
    user_account.add_transaction(
        transaction_type=args.type,
        amount=args.amount,
        timestamp=args.timestamp,
        source_account=args.source_account
    )
    print("Transaction added successfully!")
    print("Transaction History:")
    for transaction in user_account.transaction_history:
        print(transaction)
   
if __name__ == '__main__':
    main()


class OnlineBankingSystem:
    def __init__(self):
        self.user_account= {}

    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    def create_bank_account(self, firstname, lastname, email, initial_balance=0, account_type='Savings'):
        bank_account_number = self.generate_account_number()

        user_information = {
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "account_number": bank_account_number,
            "balance": initial_balance,
            "account_type": account_type
     }
    
        self.user_account[bank_account_number]= user_information

        print(f"\n Congratulations on making your new online banking account! Here are your account details:")
        print(f"Account Number: {bank_account_number}")
        print(f"Name: {firstname} {lastname}")
        print(f"Email: {email}")
        print(f"Initial Balance: ${initial_balance}")
        print(f"Account Type: {account_type}")

        return bank_account_number


class CheckBalance:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The deposit is ${amount}, so the new balance is: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"The withdrawal amount is ${amount}. The new balance is ${self.balance}.")
        else:
            print(f"There is not enough money in your bank account.")
            
    def get_balance(self):
       return self.balance if self.balance > 0 else -self.balance

import re

def validate_password(password):
    # Checks length and character requirements (One uppercase letter, One lowercase letter, One digit is required) 
    return len(password) >= 7 and re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]+$", password)


password = input("Enter your password: ")

# password validation check using conditional statement 
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")


def validate_password(self, password):
        # Use regex to validate password
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$', password):
            return True
        else:
            return False


