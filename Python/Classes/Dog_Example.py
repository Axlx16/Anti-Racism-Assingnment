#This is an example from the video: https://www.youtube.com/watch?v=JeznW_7DlB0
#This is a very basic example of how a class works
class Dog:
    #__init__ function is always passed when class is created
    # self here refers to the instance of the class
    def __init__(self, name, age): #as __init__ is always passed when the class in created self serves to acess variables
        self.dog_name = name #
        self.dog_age = age
    

    # using the __init__ function allows you to call the function get_name without passing any permiters (as perimeters are defined when an instance of the class in created due to __init__)

    def get_name(self):
        return self.dog_name #returning variable what the name was passed through the class (but as a variable self.dog_name)
        
    def get_age(self):
        return self.dog_age #returning variable what the name was passed through the class (but as a variable self.dog_age)
    
    
dog_1 = Dog('Alex', 13) #__init__ requires 2 paremeters
print(dog_1.get_name()) 
print(dog_1.get_age())

