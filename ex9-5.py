"""
"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
"""
# Users

class User:
    """User creation class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name}! Welcome back.")
        
        
    def login_attempts_desc(self):
        print(f'Login Attempts: {self.login_attempts}')
        
    def login_attempts_increment(self):
        self.login_attempts += 1
        

adam_smith = User("adam", "smith", 20)


#adam_smith.describe_user()
#adam_smith.greet_user()

adam_smith.login_attempts_desc()
adam_smith.login_attempts_increment()
adam_smith.login_attempts_increment()
adam_smith.login_attempts_increment()
adam_smith.login_attempts_desc()




