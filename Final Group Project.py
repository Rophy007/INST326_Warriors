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
