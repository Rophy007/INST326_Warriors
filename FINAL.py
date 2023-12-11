


















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
