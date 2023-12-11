import json
import csv
import hashlib
import random
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re


class UserError(Exception):
    pass

class UserRegistrationError(Exception):
    pass

class UserLoginError(Exception):
    pass

class TransactionError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.user_data_file = 'user_data.csv'
        self.logged_in_user = None
        self.user_accounts = self.load_user_data()

    def create_account(self):
        print("Create a new account:")
        user_info = {
            "first_name": input("Enter your first name: "),
            "last_name": input("Enter your last name: "),
            "dob": input("Enter your date of birth (YYYY-MM-DD): "),
            "username": input("Choose a username: "),
            "hashed_password": self.hash_password(input("Enter a password: ")),
            "balance": 0
        }

        self.user_accounts[user_info['username']] = {"balance": 0}
        self.write_to_csv(user_info)
        print("Account created successfully!")

    def load_user_data(self):
        user_accounts = {}
        with open(self.user_data_file, 'r') as file:
            reader = csv.DictReader(file, fieldnames=["first_name", "last_name", "dob", "username", "hashed_password", "balance"])
            next(reader)  # Skip the header row

            for row in reader:
                username = row['username']
                balance = float(row.get('balance', 0.0))
                user_accounts[username] = {"balance": balance}

        return user_accounts

    def write_to_csv(self, user_info):
        with open(self.user_data_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=user_info.keys())
            writer.writerow(user_info)

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



    def show_account_options(self):
        while True:
            print("\nAccount Options:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Log out")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.deposit(float(input("Enter the deposit amount: ")))
            elif choice == '2':
                self.withdraw(float(input("Enter the withdrawal amount: ")))
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                print("Logging out...")
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def deposit(self, amount):
        self.user_accounts[self.logged_in_user]["balance"] += amount
        self.update_csv()

    def withdraw(self, amount):
        if self.user_accounts[self.logged_in_user]["balance"] >= amount:
            self.user_accounts[self.logged_in_user]["balance"] -= amount
            self.update_csv()
        else:
            print("Insufficient funds.")

    def check_balance(self):
        balance = self.user_accounts[self.logged_in_user]["balance"]
        print(f"Current Balance: {balance}")

    def update_csv(self):
        with open(self.user_data_file, 'r') as file:
            reader = csv.DictReader(file)

            rows = []
            for row in reader:
                username = row['username']
                if username in self.user_accounts:
                    row['balance'] = self.user_accounts[username]['balance']
                rows.append(row)

        with open(self.user_data_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "dob", "username", "hashed_password", "balance"])
            writer.writeheader()
            writer.writerows(rows)

class UserAccount:
    def __init__(self, username, firstname, lastname, email, account_type='Savings', initial_balance=0):
        self.username = username
        self.account_number = self.generate_account_number()
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.account_type = account_type
        self.balance = initial_balance

        self.transaction_history = pd.DataFrame(columns=['Type', 'Amount', 'Timestamp'])

    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        new_transaction = pd.DataFrame({
            "Type": [transaction_type],
            "Amount": [amount],
            "Timestamp": [timestamp]
        })

        self.transaction_history = pd.concat([self.transaction_history, new_transaction], ignore_index=True, sort=False)

    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Invalid deposit amount. Amount must be greater than 0.")
        self.balance += amount
        self.add_transaction(transaction_type='Deposit', amount=amount)
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

        if self.balance > 1000:
            print("Oh, you got money!")

    def withdraw(self, amount):
        if amount <= 0:
            raise TransactionError("Invalid withdrawal amount. Amount must be greater than 0.")
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction(transaction_type='Withdrawal', amount=amount)
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")
        print("Transaction History:")

        sorted_history = sorted(self.transaction_history.to_dict(orient='records'), key=lambda x: x['Amount'])

        print(pd.DataFrame(sorted_history)[['Type', 'Amount', 'Timestamp']])

        if not self.transaction_history.empty:
            transaction_types = self.transaction_history['Type'].tolist()
           
            # 6. visualizing data table
            plt.figure(figsize=(10, 6))
            sns.barplot(data=self.transaction_history, x='Type', y='Amount', hue='Type', estimator=sum)
            plt.title('Transaction History')
            plt.xlabel('Transaction Type')
            plt.ylabel('Amount')
            plt.show()

def validate_password(self, password):
        # Use regex to validate password
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$', password):
            return True
        else:
            return False

class TransactionModule:
    def __init__(self, online_banking_system, username):
        self.online_banking_system = online_banking_system
        self.username = username

    def run_transaction_module(self):
        try:
            while True:
                print("\nChoose a transaction:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")

                choice = input("Enter your choice (1/2/3/4): ")

                if choice == '1':
                    amount = float(input("Enter deposit amount: "))
                    print(f"Initiating deposit of ${amount} for user {self.username}")
                    self.online_banking_system.user_accounts[self.username].deposit(amount)
                elif choice == '2':
                    amount = float(input("Enter withdrawal amount: "))
                    print(f"Initiating withdrawal of ${amount} for user {self.username}")
                    self.online_banking_system.user_accounts[self.username].withdraw(amount)
                elif choice == '3':
                    print(f"Checking balance for user {self.username}")
                    self.online_banking_system.user_accounts[self.username].check_balance()
                elif choice == '4':
                    print("Exiting transaction module. Goodbye!")
                    self.online_banking_system.save_user_data()
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")

        except TransactionError as e:
            print(f"Transaction Error: {e}")


class OnlineBankingSystem:
    def __init__(self):
        self.user_accounts = {}

    def load_user_data(self):
        try:
            with open('user_data.json', 'r') as file: #8. using with statement
                user_data = json.load(file) #9. using json.load
                self.user_accounts = {
                    username: UserAccount(username, *(data.get(key, default) for key, default in [
                        ('firstname', ''),
                        ('lastname', ''),
                        ('email', ''),
                        ('account_type', 'Savings'),
                        ('balance', 0)
                    ]))
                    for username, data in user_data.items()
                }
        except FileNotFoundError:
            pass

    def save_user_data(self):
        user_data = {}
        for username, user in self.user_accounts.items():
            user_data[username] = {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'email': user.email,
                'account_type': user.account_type,
                'balance': user.balance,
                'transaction_history': user.transaction_history.to_dict(orient='records')
            }
        with open('user_data.json', 'w') as file:
            json.dump(user_data, file, indent=2)

    def validate_password(self, password):
        # print(f"Validating password for user with length {len(password)}")
        return len(password) >= 7
    
    def __str__(self):
        balance_message = "Oh, you got money!" if self.balance > 1000 else ""
        return f"UserAccount(username={self.username}, account_number={self.account_number}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"email={self.email}, account_type={self.account_type}, balance={self.balance}) {balance_message}"
    
    def create_bank_account(self):
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        email = input("Enter your email: ")

        print("\nChoose the type of account:")
        print("1. Savings")
        print("2. Checking")

        account_type_choice = input("Enter your choice (1/2): ")

        if account_type_choice == '1':
            account_type = 'Savings'
        elif account_type_choice == '2':
            account_type = 'Checking'
        else:
            print("Invalid choice. Defaulting to Savings.")
            account_type = 'Savings'

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.validate_password(password):
            if username not in self.user_accounts:
                user_account = UserAccount(username, firstname, lastname, email, account_type)
                self.user_accounts[username] = user_account
                print("\nCongratulations on creating your new online banking account!")
                print(f"Account Number: {user_account.account_number}")
                print(f"Name: {user_account.first_name} {user_account.last_name}")
                print(f"Email: {user_account.email}")
                print(f"Initial Balance: ${user_account.balance}")
                print(f"Account Type: {user_account.account_type}")
                return user_account
            else:
                print("User already exists. Please log in.")
        else:
            print("Invalid password. Password must have a minimum length of 7 characters.")

if __name__ == "__main__":
    online_banking_system = OnlineBankingSystem()
    online_banking_system.load_user_data()

    print("Welcome to the Online Banking System!")

    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Log In")
        print("3. Exit")

        option = input("Enter your choice (1/2/3): ")

        if option == '1':
            online_banking_system.create_bank_account()
        elif option == '2':
            username = input("Enter your username: ")
            if username in online_banking_system.user_accounts:
                password = input("Enter your password: ")
                if online_banking_system.user_accounts[username].validate_password(password):
                    online_banking_system.save_user_data()
                    online_banking_system.load_user_data()
                    transaction_module = TransactionModule(online_banking_system, username)
                    transaction_module.run_transaction_module()
                    online_banking_system.save_user_data()
                else:
                    print("Invalid password. Please try again.")
            else:
                print("User does not exist. Please create an account.")
        elif option == '3':
            print("Exiting Online Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
