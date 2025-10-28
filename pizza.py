import math

# --- Helper Functions ---

def get_number_of_people():
    while True:
        numberofpeople = int(input('Enter number of guests: '))
        if numberofpeople >= 1:
            return numberofpeople
        else:
            print("Please enter at least 1 person.")


def get_appetite_level():
    while True:
        appetite = int(input('Enter the level of appetite\n(1 - not hungry, 2 - medium appetite, 3 - hungry): '))
        if appetite == 1:
            return 2, appetite
        elif appetite == 2:
            return 3, appetite
        elif appetite == 3:
            return 4, appetite
        else:
            print('\nTry again rating from 1 to 3!')


def get_pizza_size():
    while True:
        pizzasize = int(input('Enter the pizza size:\n(1 - small, 2 - medium, 3 - large): '))
        if pizzasize == 1:
            return 6, 8.99, "Small", pizzasize
        elif pizzasize == 2:
            return 8, 12.99, "Medium", pizzasize
        elif pizzasize == 3:
            return 12, 16.99, "Large", pizzasize
        else:
            print('\nTry again ordering available pizza sizes! ')


def calculate_total_slices(people, slices_per_person):
    return people * slices_per_person


def calculate_pizzas_needed(total_slices, slices_per_pizza):
    return math.ceil(total_slices / slices_per_pizza)


def calculate_total_cost(num_pizzas, price_per_pizza):
    return float(num_pizzas * price_per_pizza)


def calculate_cost_per_person(total_cost, people):
    return total_cost / people


def calculate_leftover_slices(num_pizzas, slices_per_pizza, total_slices):
    return (num_pizzas * slices_per_pizza) - total_slices


def display_results(people, appetite, slices_per_person, pizzasize, pizzasize_name,
                    num_pizzas, total_cost, cost_per_person, leftovers):
    pizza_pizzas = "pizza" if num_pizzas == 1 else "pizzas"
    print(f'''
People: {people}
Appetite: {appetite} ({slices_per_person} slices each)
Size: {pizzasize} ({pizzasize_name})
Expected: {num_pizzas} {pizza_pizzas}, ${total_cost:.2f} total, ${cost_per_person:.2f} per person, {leftovers} leftover.
    ''')


# --- Main Function ---
def main():
    people = get_number_of_people()
    slices_per_person, appetite = get_appetite_level()
    slices_per_pizza, price_per_pizza, pizzasize_name, pizzasize = get_pizza_size()

    total_slices = calculate_total_slices(people, slices_per_person)
    num_pizzas = calculate_pizzas_needed(total_slices, slices_per_pizza)
    total_cost = calculate_total_cost(num_pizzas, price_per_pizza)
    cost_per_person = calculate_cost_per_person(total_cost, people)
    leftovers = calculate_leftover_slices(num_pizzas, slices_per_pizza, total_slices)

    display_results(people, appetite, slices_per_person, pizzasize, pizzasize_name,
                    num_pizzas, total_cost, cost_per_person, leftovers)


# --- Program Entry Point ---
if __name__ == "__main__":
    main()
