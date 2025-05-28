class Animal(object):
    def __init__(self):
       self.age = 0
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Pet(Dog, Cat):
    def __init__(self,animal_type=None):
        super().__init__()
        self.pet_name = "Unknown"
        if animal_type == "dog":
            self.animal_type = Dog()
        elif animal_type == "cat":
            self.animal_type = Cat()
    def set_name(self,name):
        self.pet_name = name
    def speak(self):
        return f"{self.pet_name} says {self.animal_type.speak()}"
pet = Pet("dog")
pet.set_name("Buddy")
print(pet.speak())
pet = Pet("cat")
pet.set_name("Molly")
print(pet.speak())

#=============================


class Animal:
    def __init__(self):
        self.age = 0

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# 定义Dog类，继承自Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# 定义Cat类，继承自Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# 定义Pet类，同时继承自Dog和Cat
class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()  # 调用基类Animal的构造函数
        self.pet_name = "Unknown"
    def set_name(self, name):
        self.pet_name = name
    def speak(self):
        return f"{self.pet_name} says {super().speak()}"
"""
super()函数会按顺序调用，这里调用Dog().speak()
"""
my_pet = Pet()
my_pet.set_name("Buddy")
print(my_pet.speak())