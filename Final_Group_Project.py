import json

class User(Exception):
    pass

def login(username, password):
    try:
        # Load user data from a JSON file
        with open('user_data.json', 'r') as file:
            users = json.load(file)

        if username not in users:
            raise User("Invalid username")

        if users[username]['password'] == password:
            return True 
        else:
            raise User("Invalid password")

    except FileNotFoundError:
        raise User("User data not found. Please register an account.")

if __name__ == "__main__":
    try:
        # Get user inputs
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")

        # Attempt login
        if login(username_input, password_input):
            print("Login successful!")
        else:
            print("Login failed.")

    except User:
        print(f"Error") 

class UserAccount:
   
    def __init__(self):
        self.transaction_history = []  """ Initialize transaction history """

    def add_transaction(self, transaction_type, amount, timestamp, source_account=None):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "timestamp": timestamp,
            "source_account": source_account
        }
        self.transaction_history.append(transaction)

user_account = UserAccount() """ creating instance """
user_account.add_transaction("deposit", 100, "2023-11-15", source_account=None) """ adding a transaction """


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


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The deposit is ${amount}, so the new balance is: ${self.balance})

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"The withdrawal amount is ${amount}. The new balance is ${self.balance}.")
        else:
            print(f"There is not enough money in your bank account.")
   
   def get_balance(self):
       return self.balance
