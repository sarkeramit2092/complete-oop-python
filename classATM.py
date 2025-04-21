#constructor - __init__
#It is a special method that contains code which gets executed automatically when an object is created from the class.

class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
        Hello, How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        Your choice: """)

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit()
            
            elif user_input == "3":
                self.withdraw()

            elif user_input == "4":
                self.check_balance()
            
            elif user_input == "5":
                print("Bye! Have a nice day.")
                break

            else:
                print("Invalid choice. Please try again.")

    def create_pin(self):
        self.pin = input("Set your pin: ")
        print("Pin set successfully.")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid pin.")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid pin.")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid pin.")

# Create an ATM instance
Bracbank = Atm()
