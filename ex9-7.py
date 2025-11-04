class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")

    def login_attempts_increment(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def login_attempts_desc(self):
        print(f"{self.first_name} has {self.login_attempts} login attempts.")


class Admin(User):
    def __init__(self, first_name, last_name, age, privileges=None):
        super().__init__(first_name, last_name, age)
        #Default privilegiebis minicheba
        if privileges is None:
            self.privileges = ['Can add user', 'Can delete user', 'Can ban user']
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Example usage
adam_smith = User('Adam', 'Smith', 30)
adam_smith.login_attempts_increment()
adam_smith.login_attempts_desc()

new_admin = Admin('Nino', 'Gevorkyan', 22)
new_admin.describe_user()
new_admin.show_privileges()
