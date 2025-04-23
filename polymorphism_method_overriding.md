# Polymorphism 

- Polymorphism is one of the core concepts of Object-Oriented Programming (OOP), and it refers to the ability of a single function, method, or operator to behave differently based on the context or the objects it is operating on.

The word "Polymorphism" comes from:
Poly = many

Morph = forms

➡️ So, Polymorphism means "many forms."

There are mainly two types of polymorphism in programming:

1. Compile-time Polymorphism (Static Binding)
Also called method overloading or operator overloading.
It happens when multiple functions with the same name exist but with different parameters.

🛠 Example in Java:

```java

class MathOps {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```
2. Run-time Polymorphism (Dynamic Binding)
Also called method overriding.
It occurs when a subclass provides a specific implementation of a method that is already defined in its parent class.

🛠 Example in Python:

```python

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism in action
def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Output: Dog barks
make_sound(Cat())  # Output: Cat meows

```
# Why is polymorphism useful?
Promotes code reuse

Makes code more flexible and extensible

Supports clean architecture and design patterns
---------------------------------------------------------------------------------------------------------
![poly-1](image-19.png)

![poly-output](image-20.png)


- This is called method overriding - and which is one type of a Polymorphism.