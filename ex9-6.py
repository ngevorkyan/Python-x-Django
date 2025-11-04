class Restaurant:
    """This class creates the restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and cuisine type of restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0
        
    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Indicates that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")
        
    def describe_visitor_amount(self):
        """Describes visitor amount"""
        print(f'Visitors: {self.numbers_served}')  
              
    def set_numbers_served(self, new):
        """Sets or updates the number of visitors"""
        self.numbers_served = new
        
    def increment_number(self, increment):
        """Increments visitor amount"""
        self.numbers_served += increment


class IceCreamStand(Restaurant):
    """A specific kind of Restaurant that serves ice cream."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def display_flavors(self):
        """Displays all available ice cream flavors"""
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_stand = IceCreamStand('Sanakine', 'nakinebi', ['vanilla', 'chocolate', 'strawberry'])
my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.describe_visitor_amount()
my_stand.display_flavors()
