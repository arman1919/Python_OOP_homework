from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def  eat(self):
        pass


class Cat(IAnimal):
    def speak(self):
        print("Miau-Miau")

    def eat(self):
        print("Mouse")

class Dog(IAnimal):
    def speak(self):
        print("Haf-Haf")

    def eat(self):
        print("Bone")


cat = Cat()

cat.speak()

cat.eat()

dog = Dog()

dog.speak()

dog.eat()

