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
