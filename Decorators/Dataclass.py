from dataclasses import dataclass, field
from typing import List

@dataclass(
    order=True,       # Enable comparison methods (__lt__, __eq__, etc.)
    frozen=True,      # Make instances immutable
    init=True,        # Generate __init__ method
    repr=True,        # Generate __repr__ method
    eq=True,          # Generate __eq__ method
    unsafe_hash=False # Disable automatic generation of __hash__ method
)
class Person:
    name: str
    age: int
    emails: List[str] = field(default_factory=list, metadata={'description': 'List of email addresses'})

# Create instances of Person
person1 = Person("Alicia", 30, ["example@example.com", "alicia@gmail.com"])
person2 = Person("Unknown", 25, ["unknown@example.com"])

# Access attributes
print(person1.name)   # Output: Alice
print(person1.age)    # Output: 30
print(person1.emails) # Output: ['alice@example.com', 'alice@gmail.com']

# Comparing instances (due to `order=True` and `frozen=True`)
print(person1 < person2)  # Output: False

# Attempting to modify a frozen instance raises an error
# person1.age = 35  # This will raise an error

# Access metadata for the emails field
print(Person.__dataclass_fields__['emails'].metadata['description'])  # Output: List of email addresses
person1.__repr__()