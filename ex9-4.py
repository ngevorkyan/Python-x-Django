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
        self.numbers_served = 0
        
    def describe_visitor_amount(self):
        '''describes visitor amount'''
        print(f'Visitors: {self.numbers_served}')  
              
    def set_numbers_served(self, new):
        '''Sets u update the value'''
        self.numbers_served = new
        
    def increment_number(self,increment):
        '''increments visitor amount'''
        self.numbers_served += increment
        
        
        
restaurant = Restaurant('Chame genacvale', 'Georgian')

#Before
restaurant.describe_visitor_amount()

#After Overwriting
restaurant.numbers_served = 30
restaurant.describe_visitor_amount()

#After Setting New Value
restaurant.set_numbers_served(100)
restaurant.describe_visitor_amount()

#After Incrementing New Value
restaurant.increment_number(100)
restaurant.describe_visitor_amount()








