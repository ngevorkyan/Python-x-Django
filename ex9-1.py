
"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""

#Resaurant

class Restaurant:
    """This class creates the restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and cuizine type of restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """describe the restaurant attribuites"""
        print(f'The restaurant is called "{self.restaurant_name}", it has a {self.cuisine_type} cuisine.')
        
    def open_restaurant(self):
        """Simulate opening the restaurant"""
        print(f'{self.restaurant_name} is now open')
        
restaurant = Restaurant('Chame genacvale', 'Georgian')

print(f'Name: {restaurant.restaurant_name}')
print(f'Cuisine: {restaurant.cuisine_type}\n')

restaurant.describe_restaurant()
restaurant.open_restaurant()