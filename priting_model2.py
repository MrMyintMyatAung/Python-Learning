
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    144 Chapter 8
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        curren_design = unprinted_designs.pop()
        print(f"Printing model: {curren_design}")
        completed_models.append(curren_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
