class Dog:
    """The simple attempt to model a dog"""

    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def bark(self):
        """Prints out a bark"""
        print("Woof!")

    def sit(self):
        """Print out a sit command"""
        print(f"{self.name} is sitting!")        


    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.bark()
my_dog.sit()
my_dog.roll_over()