class Animal:
    def __init__(self, name):
        self.name = name

    def reply(self):
        self.speak()


class Mammal(Animal):
    pass


class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"


class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Bark!"


class Primate(Mammal):
    def speak(self):
        return f"Hello, my name is {self.name}."


class ComputerScientist(Primate):
    pass


dog = Dog("Bob")
print(dog.speak())
computer_scientist = ComputerScientist("Calista")
print(dir(computer_scientist))
print(computer_scientist.name)
print(computer_scientist.speak())
