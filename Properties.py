class Person:
    def __init__(self,name,age) -> None:
        self._age = age
        self._name = name

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age (self,age):
        if not age:
            raise ValueError("Age cant be empty")
        
        self._age = age
    

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Name cant be empty")
        self._name = name

    
human = Person("Bob",20)

print(human.name)

human.name = "Alexs"

print(human.name)

print(human.age)

human.age = 21

print(human.age)
