class MyClass:
    class_variable = "Class Variable"

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, string):
        # This method creates a new instance of MyClass from a string
        value = int(string)  # Convert string to int
        return cls(value)  # Create and return a new instance of MyClass

    @classmethod
    def modify_class_variable(cls, new_value):
        cls.class_variable = new_value

# Create an instance using a class method
instance = MyClass.from_string("10")
print(instance.value)  # Output: 10

# Access class variable through class method
print(MyClass.class_variable)  # Output: Class Variable

# Modify class variable using class method
MyClass.modify_class_variable("New Class Variable")
print(MyClass.class_variable)  # Output: New Class Variable
