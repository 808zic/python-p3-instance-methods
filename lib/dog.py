#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
     def bark(self):
        #self allows methods to access the other methods and attributes
        print("Woof!")

     def sit(self):
        print("The dog is sitting.")



fido = Dog()
fido.bark()

snoopy = Dog()
snoopy.sit()





#The Behavior of Objects
#Dot Notation
'''
class Dog:
    pass

fido = Dog()
# <__main__.Dog object at 0x1027f07f0>

fido.__dir__()
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__
The __dir__() method provides you with a list of the object's methods and attributes

'''