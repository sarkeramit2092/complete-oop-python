## Aggregation is a "has-a" relationship where one class contains a reference to another class, but both can exist independently.

"Has-a" is a way to describe a relationship between two classes where:

One class contains or uses another class.

It means ownership or association, not inheritance.

- Example:
If a Car has a Engine, it means:

```python

class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
```
Here, Car has-a Engine.

It's different from "is-a", which is used in inheritance:

```python

class Animal:
    pass

class Dog(Animal):  # Dog is-a Animal
    pass

```

```
Has-a = uses/contains (like aggregation or composition)

Is-a = inherits from (like subclassing)
```

``` python

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

# Creating address instance
add = Address("Kolkata", 700156, "WB")

# Aggregating address with customer
cust = Customer("Nitish", "Male", add)

# Updating customer profile and address
cust.edit_profile("Ankit", "Gurgaon", 122011, "Haryana")

# Printing updated address pincode
print(cust.address.pincode)

```

🔍 Explanation: Aggregation Relationship
Aggregation is a type of association where one class (the "whole") has a reference to another class (the "part"), but both can exist independently.

In this case:

- Customer is the "whole".

- Address is the "part".

- Customer has an Address, passed during initialization and stored in self.address.

Even if the Customer object is deleted, the Address object can exist independently (unless explicitly tied).

So this is aggregation, not composition. In composition, the part’s life cycle depends on the whole.

✅ Example of Aggregation:

```python

add = Address("Kolkata", 700156, "WB")  # Independent address object
cust = Customer("Nitish", "Male", add)  # Aggregated into Customer

```