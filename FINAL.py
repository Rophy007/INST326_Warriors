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
    """
    Manages user accounts within the system.
    """

    def __init__(self):
        """
        Claim: Tyrese
        Technique: N/A
        
        Initializes the UserManager object.

        Attributes:
        user_data_file (str): The file path for storing user data.
        logged_in_user (str): Username of the currently logged-in user.
        user_accounts (dict): Dictionary containing user accounts and their details.
        """
        self.user_data_file = 'user_data.csv'
        self.logged_in_user = None
        self.user_accounts = self.load_user_data()

    def create_account(self):
        """
        Claim: Tyrese
        Technique: N/A
        Creates a new user account.

        Prompts the user to enter details and creates a new account based on the input.
        """
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
        """
        Claim: Tyrese
        Technique: N/A
        
        Loads user data from the file.

        Reads the user data from the CSV file and returns a dictionary of user accounts.
        """
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
        """
        Claim: Tyrese
        Technique: N/A
        Writes user information to the CSV file.

        Appends user information to the CSV file for storage.

        Parameters:
        user_info (dict): Dictionary containing user information.
        """
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
        Claim: Abrar
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
        Claim: Abrar
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
        Claim: Abrar
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






















































































    def add_transaction(self, transaction_type, amount):
         '''
        Claim: Rophy 
        
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

















































































































































































































def __str__(self):
"""
Claim: Rophy 
This provides a string representation of an object. It checks if the balance attribute of t he UserACcount if greaters than 1000.
If true it will print out a special message

Parameters: (self)

Returns: (str)
"""     
        balance_message = "Oh, you got money!" if self.balance > 1000 else ""
        return f"UserAccount(username={self.username}, account_number={self.account_number}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"email={self.email}, account_type={self.account_type}, balance={self.balance}) {balance_message}"
    
    def create_bank_account(self):

"""
Claim: Rophy 
This function creates a new user account, provides feedback to the user. 

Parameters: self 

Returns: THe created UserAccount class  
"""
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

"""
Claim: Rophy 
This is a basic level interface for the users of the online banking system. 
It creates accounts, log in, and perfrom transactions 

Parameters: int or float

Return: (str)

"""
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
