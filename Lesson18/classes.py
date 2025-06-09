# Classes are like the blueprints when we want to create something
class Vehicle: 
    def __init__(self, make, model): #Self is represented as the object that is created
        self.make = make
        self.model = model

    def moves(self): # Self is referred to itself
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3') # We can add like this too

print(my_car.make)
print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Ace')
your_car.get_make_model()
your_car.moves()