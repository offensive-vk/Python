from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def calculate_salary(self):
        pass

# Concrete subclasses
class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, age, hours_worked, rate_per_hour):
        super().__init__(name, age)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour

# Create instances and call methods
full_time_emp = FullTimeEmployee("Alice", 30, 50000)
part_time_emp = PartTimeEmployee("Bob", 25, 20, 15)

print("Full-time employee salary:", full_time_emp.calculate_salary())  # Output: 50000
print("Part-time employee salary:", part_time_emp.calculate_salary())  # Output: 300
