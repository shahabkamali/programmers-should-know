

class Dog:

    """ A simple dog class"""

    def __str__(self):
        return "Dog"

    def speak(self):
        return "woof!" 


class Cat:

    """ A simple cat class"""
    def __str__(self):
        return "Cat"

    def speak(self):
        return "meow!"  


class PetStore():
    """PetStore houses our Abstract factory"""
    
    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """
        
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the object b y the Dog factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("our pet is '{}' !".format(pet))
        print("our pet says hello by '{}'".format(pet.speak()))
        print ("its food is '{}'!".format(pet_food))

class DogFactory:
    def get_pet(self):
        """ Returns a dog object """
        return Dog()

    def get_food(self):
        """returns a dog food object"""
        return "Dog food!"

# create a concrete factory
factory = DogFactory()

# create a pet store haousing our abstract factory
shop = PetStore(factory)


# Invoke the utility method to show the details of our pet
shop.show_pet()
