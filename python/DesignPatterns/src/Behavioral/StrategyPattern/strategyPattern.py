
import types  # Import the types module

class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function = None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function

    def execute(self): # This gets replaced by another verion if another strategy is provided
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create our default strategy
s0 = Strategy()

# Lets execute our default strategy
s0.execute()

#Let's create the first variation of our default strategy byt providing a new behavior
s1 = Strategy(strategy_one)

# Let's execute the strategy
s1.name = "Strategy One"
#Let's execute the strategy
s1.execute()

s2 = Strategy()
s2.name = "Strategy two"
s2.execute()