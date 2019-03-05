
class DrawingAPIOne(object):
    """ Impelementation-specific abstraction: concrete class one"""
    def draw_circle(self,x, y, radius):
        print("API 1 drawing a circle at ({}, {}, with radius {})!".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementtation-specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {}, with radius {})!".format(x, y, radius))


class Circle(object):
    """Impelemetation-indepednent abstraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""

        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Impelementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent

#Biuld the first Circle object using API One
cirlce1 = Circle(1,2,3, DrawingAPIOne())

#Draw a circle
cirlce1.draw()

#Biuld the second Circle object using API Two
cirlce2 = Circle(1,2,3, DrawingAPITwo())

cirlce2.draw()
