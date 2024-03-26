class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Error: Division by zero!")

# Example usage:
print("Addition:", MathOperations.add(5, 3))
print("Subtraction:", MathOperations.subtract(7, 4))
print("Multiplication:", MathOperations.multiply(2, 6))
print("Division:", MathOperations.divide(10, 2))
print("Division:", MathOperations.divide(10, 0))
