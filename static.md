🔹 Class Variables
Shared across all instances of the class.

Defined inside the class, but outside any methods.

Good for constants or values common to all objects.

```python

class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Canis lupus familiaris
```
🔹 Class Methods
Use the @classmethod decorator.

Take cls as the first parameter instead of self.

Can access and modify class variables.

Called on the class itself, not just an instance.

```python

class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

Dog.change_species("Canis lupus familiaris")
print(Dog.species)  # Canis lupus familiaris

```
🔸 Bonus: Static Methods
Use @staticmethod decorator.

No self or cls required.

Behaves like a regular function but lives in the class namespace.

```python

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))  # 8

```

```python

class Atm:
    __counter = 1  # private class variable

    def __init__(self):
        # instance variables
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter += 1

        print(id(self))
        # self.__menu()  # Uncomment if __menu method exists

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new  # Accessing the correct class variable
        else:
            print("Not allowed")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if type(amount) == int and amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

# Example usage
atm1 = Atm()
atm2 = Atm()

print("Current Counter:", Atm.get_counter())

Atm.set_counter(100)
print("Counter after setting:", Atm.get_counter())

# Setting and getting pin
atm1.set_pin("1234")
print("ATM1 PIN:", atm1.get_pin())

```