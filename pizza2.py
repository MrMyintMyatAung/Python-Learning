def make_pizza(size, *toppings):
    """Make a pizza with the given size and toppings."""
    """Summarize the pizza we are about to make."""
    
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')