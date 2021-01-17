# Defining the class for a Object_Ball.
class Object_Ball:
    
    def __init__(self, name, color, shape, size):
        self.name = name
        self.color = color
        self.shape = shape
        self.size = size

    def getDetails(self):
        print("Name : " + self.name)
        print("Color : " + self.color)
        print("Shape : " + self.shape)
        print("Size : " + self.size)
        

# Creating an instance
Object_Volleyball = Object_Ball("Volleyball", "Yellow", "Sphere", "Medium")
Object_Volleyball.getDetails()
