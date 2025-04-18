from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


#for obj creation of this class we must have to implement all abstract methods
class Human(Animal):
    def move(self):
        print("Walking in 2 legs")


#for obj creation of this class we must have to implement all abstract methods
class Dog(Animal):
    def move(self):
        pass


#If we are not implementing all the abstract methods in this class then we can't create an obj for this class
class Cat(Animal):
    pass


H = Human()
H.move()

D = Dog()
D.move()

C = Cat()
