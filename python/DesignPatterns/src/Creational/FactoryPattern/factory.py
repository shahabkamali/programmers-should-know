from abc import ABC, abstractmethod

class AnimalBaseClass(ABC):
    def __init__(self, name=None):
        if name:
            self.name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Cat(AnimalBaseClass):
    def __init__(self, name=None):
        AnimalBaseClass.__init__(self, name)

    def speak(self):
        print('meowwww! :3')

    def move(self):
        print('the cat walks')

    def purr(self):
        print('purrrrr!<3')


class Dog(AnimalBaseClass):
    def __init__(self, name=None):
        AnimalBaseClass.__init__(self, name)

    def speak(self):
        print('woof, woof! :3')

    def move(self):
        print('the dog walks')


# factory method
def get_pet(pet="dog"):
    """ the factory method """

    pets = dict(dog=Dog("Hope"), cat=Cat("peace"))

    return pets[pet]

d = get_pet("dog")

# returns dog speak function
d.speak()
