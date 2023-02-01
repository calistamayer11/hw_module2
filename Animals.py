class Animal:
    """Animal class"""

    def __init__(self, name):
        """Initializes animal class"""
        self.name = name

    def reply(self):
        """Calls speak method on the object"""
        self.speak()


class Mammal(Animal):
    """Mammal class (methods are on Animal super class)"""

    pass


class Cat(Mammal):
    """Cat class"""

    def speak(self):
        """Returns the speak method of cat class"""
        return f"{self.name} says Meow!"


class Dog(Mammal):
    """Dog class, has Mammal super class"""

    def speak(self):
        """Returns the speak method of dog class"""
        return f"{self.name} says Bark!"


class Primate(Mammal):
    """Primate class"""

    def speak(self):
        """Returns the speak method of primate class"""
        return f"Hello, my name is {self.name}."


class ComputerScientist(Primate):
    """Computer Scientist class"""

    pass
