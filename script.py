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

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email.strip().replace(" ", "").lower()
    
    def set_email(self, new_email):
        self._email = new_email
    
user1 = User("danteman", " Dan@gmail.com  ", "123")
print(user1.get_email())

user1.set_email("danny@outlook.com")
print(user1.get_email())
                