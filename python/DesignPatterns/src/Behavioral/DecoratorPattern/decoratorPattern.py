from functools import wraps

def make_blink(function):
    """Defines the decorator"""
    
    #This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    
    #Define the inner function
    def decorator():
        #Grab the return value of the funtion bering decorated
        ret = function()

        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


#Apply the decorator here!

@make_blink
def hello_world():
    """Original function!"""
    
    return "hello, world"


print(hello_world())

print(hello_world.__name__)

print(hello_world.__doc__)

    
