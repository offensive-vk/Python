class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter method for radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for radius"""
        if value <= 0:
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    @property
    def area(self):
        """Calculate the area of the circle"""
        return 3.14 * self._radius ** 2

    @property
    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * 3.14 * self._radius

# Create an instance of Circle
circle = Circle(5)

# Access radius using the property getter
print("Radius:", circle.radius)

# Access area using the property
print("Area:", circle.area)

# Access circumference using the property
print("Circumference:", circle.circumference)

# Modify radius using the property setter
circle.radius = 7
print("New Radius:", circle.radius)
print("New Area:", circle.area)
print("New Circumference:", circle.circumference)
