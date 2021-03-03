#This is an example from the video: https://www.youtube.com/watch?v=JeznW_7DlB0
#This focus on how inheritance of class works
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

#cat and dog classes are inheriting from pet and this is denoted with the (pet) after the class name
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #the super class is the pet class
        self.color = color

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")
    
#if a method has the same name is the lower level (child class) that method will take priorpty over the upper level class (parent class)
p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()
d = Dog("Jill", 25)
d.speak()