def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""

    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
