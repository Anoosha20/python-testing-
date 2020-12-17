# classes are user defined blueprint or prototype
# sum, multiplication, constant
# methods , class variables, instance variables, constructor etc
# objects for your classes

# **************
# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100  # class variables
# default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("Iam called automatically when object is created")
# method in class

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


# object in class


obj = Calculator(2, 3)  # syntax to create objects in class
obj.getData()
print(obj.summation())


obj1 = Calculator(4, 5)  # syntax to create objects in class
obj1.getData()
print(obj1.summation())