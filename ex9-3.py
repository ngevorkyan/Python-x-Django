"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both meth-
ods for each user.
"""
# Users

class User:
    """User creation class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name}! Welcome back.")
        

adam_smith = User("adam", "smith", 50)
emmanuel_kant = User("emmanuel", "kant", 55)
george_washington = User("george", "washington", 30)


adam_smith.describe_user()
adam_smith.greet_user()

emmanuel_kant.describe_user()
emmanuel_kant.greet_user()

george_washington.describe_user()
george_washington.greet_user()