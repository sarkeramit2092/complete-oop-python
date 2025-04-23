# Two fundamental object-oriented programming relationships:

✅ Object-Oriented Relationships

1. Inheritance (IS-A relationship)
This is a generalization/specialization relationship where one class inherits from another.

Examples:
Smartphone is a Product
Car is a Vehicle

🧠 This means Smartphone and Car inherit behavior and properties from their parent classes Product and Vehicle, respectively.

# Python code for inheritance

class Product:
    def __init__(self, name):
        self.name = name

class Smartphone(Product):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

2. Aggregation (HAS-A relationship)
This represents a "has-a" relationship where one class contains a reference to another.

Examples from the diagram:
A Customer has an Address

(This part is misgrouped in the sketch—it belongs to Aggregation)

🧠 This means a Customer object contains or is associated with an Address object.

# Python code for aggregation

class Address:
    def __init__(self, city, zip_code):
        self.city = city
        self.zip_code = zip_code

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # HAS-A relationship
Summary Table

Concept	Example Class	Relationship	Real Meaning
Inheritance	Car is-a Vehicle	IS-A	Car inherits from Vehicle
Aggregation	Customer has-a Address	HAS-A	Customer uses/contains Address
Let me know if you want a visual Python implementation of all three relationships!


✅ Inheritance (IS-A) — Smartphone inherits from Product and Car inherits from Vehicle

✅ Aggregation (HAS-A) — Customer has an Address

# Inheritance Example 1: Smartphone is a Product
class Product:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Product Name: {self.name}"

class Smartphone(Product):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def get_info(self):
        return f"{super().get_info()}, Brand: {self.brand}"

# Inheritance Example 2: Car is a Vehicle
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def get_info(self):
        return f"Vehicle with {self.wheels} wheels"

class Car(Vehicle):
    def __init__(self, wheels, model):
        super().__init__(wheels)
        self.model = model

    def get_info(self):
        return f"{super().get_info()}, Model: {self.model}"

# Aggregation Example: Customer has an Address
class Address:
    def __init__(self, city, zip_code):
        self.city = city
        self.zip_code = zip_code

    def full_address(self):
        return f"{self.city} - {self.zip_code}"

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Aggregation: HAS-A

    def get_details(self):
        return f"Customer: {self.name}, Address: {self.address.full_address()}"

# -------------------
# Testing the classes
# -------------------

# Inheritance
smartphone = Smartphone("iPhone 14", "Apple")
car = Car(4, "Tesla Model 3")

# Aggregation
address = Address("Dhaka", "1207")
customer = Customer("Sultana", address)

# Print outputs
print(smartphone.get_info())
print(car.get_info())
print(customer.get_details())

📦 Sample Output:
Product Name: iPhone 14, Brand: Apple
Vehicle with 4 wheels, Model: Tesla Model 3
Customer: Sultana, Address: Dhaka - 1207

