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
