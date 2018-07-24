# Abstraction: Properties that are hidden
# Encapsulation: Binding data and functions together which operate on that data
# Polymorphism: Same interface has different behaviors/features
# Inheritence: Getting the properties of a parent

# HW: Write a program to check if given string is right rotation of original string

""" 
Object is an instance of a class

Every object has:
-identity
-state
    -static
    -dynamic
-role/responsibilty
-behaviour

This is what makes every object of the same class unique
"""

class Human:
    """ This is the human class. This comment is the doc string """

    # static variable
    planet = "Earth"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a way to declare private member. But you can access it. use the __dict__ to see the variable assigned to it (it simply changes the name)
        self.__type_of_animal = "Social"

    # You can write anything instead of self like walk in the walk function. Python gives that freedom

    def walk(walk):
        print("{name} is Walking".format(name=walk.name))

    def __breathe(self):
        print("Breathing...")

    # invoked when we use greater than sign between objects
    def __gt__(self, another):
        return self.age > another.age

mithil = Human('Mithil', 25)
vinit = Human('Vinit', 50)

if mithil > vinit:
    print("{} is older than {}".format(mithil.name, vinit.name))
elif vinit > mithil:
    print("{} is older than {}".format(vinit.name, mithil.name))

mithil.role = "Student"

# prints out all the object variables as a dictionary
print(mithil.__dict__)
print(vinit.__dict__)

# calling private definition
mithil._Human__breathe()

# prints a list of all member functions, variables and even the private variable names
print(dir(mithil))