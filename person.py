class Person:
    # Constructor method (initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet
    def greet(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
