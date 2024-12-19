class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, value):  # Setter
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

# Example usage
person = Person("Alice")
print(person.name)  # Getter: Output -> Alice
person.name = "Bob"  # Setter
print(person.name)  # Getter: Output -> Bob
# person.name = ""  # Raises ValueError: Name cannot be empty