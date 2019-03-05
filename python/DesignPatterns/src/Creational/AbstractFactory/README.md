## Abstract Factory

 is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.




Imagine that you are creating a simulator of a furniture shop. Your code consists of:

1. Family of related products, say: Chair + Sofa + CoffeeTable.

2. Several variants of this family. For example, products Chair + Sofa + CoffeeTable available in these variants: IKEA, VictorianStyle, ArtDeco.

You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite frustrated when they receive non-matching furniture.

Also, you do not want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs very often, and you do not want to change the core code each time it happens.
