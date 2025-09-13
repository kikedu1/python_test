class Dog:
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
print(dog1.owner.name)

# dog1.bark()  # Output: "Whoof whoof!"
# print(dog1.name)  # Output: "Bruce"
# print(dog1.breed)  # Output: "Labrador"

# Another example
owner2 = Owner("Bob", "456 Puppy Ave", "555-5678")
dog2 = Dog("Freya", "Beagle", owner2)
print(dog2.owner.name)

# dog2.bark()  # Output: "Whoof whoof!"
# print(dog2.name)  # Output: "Freya"
# print(dog2.breed)  # Output: "Beagle"

