# instance variable

- jesob variables constractor er vitor thake. like:

```python

def __init__(self):
    self.pin = ""
    self.balance = 0

```

- These variables are different for every ojects.

# Encapsulation

- when we create an object from a class, it/object can access every methods and variables.

![encapsulation-1](image-4.png)

- As it can access those, it can manipulate these.

![encapsulation-2](image-5.png)

- So we have to restrict these to make them private. and this called encapsulation. 

```python

self.__pin = ""
self.__balance = 0

   def create_pin(self):
        self.__pin = input("Set your pin: ")
        print("Pin set successfully.")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.__balance += amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid pin.")
```

- we also use encapsulation for restrict methods.

```python

 self.__menu()

    def __menu(self):
        while True:
            user_input = input("""
        Hello, How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        Your choice: """)

```

- Python is the language made for adults!! 😁🤣
- Not likely two developer from india and pakistan are working on the same codebase. 🤣🤣🤣

![nothing_private](image-6.png)

 - __pin : Encapsulation is a gentalmen agreement.