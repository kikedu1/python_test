""" class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        return "Whoof whoof!"

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

# Example usage:
owner1 = Owner("Alice", "123 Dog St", "555-1234")  
dog1 = Dog("Bruce", "Labrador", owner1)
print(dog1.bark())

# dog1.bark()  # Output: "Whoof whoof!"
# print(dog1.name)  # Output: "Bruce"
# print(dog1.breed)  # Output: "Labrador"

# Another example
owner2 = Owner("Bob", "456 Puppy Ave", "555-5678")
dog2 = Dog("Freya", "Beagle", owner2)
print(dog2.owner.name)

# dog2.bark()  # Output: "Whoof whoof!"
# print(dog2.name)  # Output: "Freya"
# print(dog2.breed)  # Output: "Beagle" """

""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", "30")
person1.greet()

person2 = Person("Bob", "42")
person2.greet() """


""" class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ")

user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")

user1.say_hi_to_user(user2)
print(user1._email)

user1._email = "danny@outlook.com"
print(user1._email) """
"""
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ")

user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")

user1.say_hi_to_user(user2)
# print(user1.__email)

# user1.__email = "danny@outlook.com"
# print(user1.__email) """
""" from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def get_email(self):
        print(f"Email accesed at {datetime.now()}")
        return self.__email.strip().replace(" ", "").lower()
    
    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            print("Not a valid email")
    
user1 = User("danteman", " Dan@gmail.com  ", "123")
print(user1.get_email())

user1.set_email("432kjkj@n42")
print(user1.get_email()) """

""" class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Incorrect format")
    
user1 = User("danteman", " Dan@gmail.com  ", "123")
user1.email = "This is not an email"
print(user1.email) """


""" # Static attributes

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username : {self.username}, Email: {self.email}")


user1 = User("dantheman", "dan@gmail.com")
user2 = User("sally123", "sally@gmail.com")
user2.email= "sally4@gmail.com"

print(User.user_count)
print(user1.user_count)
print(user2.user_count)
print(user2.email) """


# Statics Methods"

""" class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance +=amount
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10)) """


class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance +=amount
            self.__log_transaction("deposit", amount) # I comparision with prior code, this will use the private method instead if statement
        else:
            print("Deposit amount must be positive")

    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}") 

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)

# account._is_valid_amount(200) # shouldn't be accessed outside of the class
# account.__log_transaction("withdraw", 300) # it's not allowed to access ouside the class

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))