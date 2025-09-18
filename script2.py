""" # Encapsulation

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount >=self._balance:
            raise ValueError("Insuficient funds.")
        self._balance -= amount
        
account = BankAccount()
print(account.balance)
account.deposit(100.99)
print(account.balance)
account.withdraw(100)
print(account.balance) """

# Abstraction - Reduce complexity by hiding unnecessary details.

""" class EmailService:

    def connect(self):
        print("Connecting to email server")

    def authenticate(self):
        print("Authenticating...")

    def send_email(self): # without abstraction, i must let public the aboveand below meths and call them one by one
        # self._connect()
        # self._authenticate
        print("Sending Email...")
        # self._disconnect()

    def disconnect(self):
        print("Disconnecting from email server...")


email = EmailService()
email.connect()
email.authenticate()
email.send_email() # with abstraction I'd only  need this statement
email.disconnect() """

# Inheritance - is a fundamental concept in oop that involves creating new classes (subclasses or derived classes) based on existing classes (superclasses or base classes)

# A car is a vhicle
# A bike is a vehicle

""" 
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def start_moto(self):
        print("Motorcycle is starting")

    def stop_moto(self):
        print("Motorcycle is stopping")

# Subclasses

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        #self.number_of_wheels = number_of_wheels


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        # self.number_of_wheels = number_of_wheels


vehicles = [
    Car("Ford", "Focus", 2008, 5), # to test inheritance, just remove the list and just instance the two objects
    Motorcycle("Honda", "Scoopy", 2018)
]
# print(car.__dict__)
# print(bike.__dict__)
# car.start()
# bike.start()

# Polymorphism - having multiple forms

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_moto()
        vehicle.stop_moto()
    else:
        raise Exception("Object is not a vehicle") """

# Coupling - degree of dependency between different classes or modules

""" class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")

class Order:
    def create(self):
        #Perform order creation logic, e.g. validate order details check producto stock, save to db etc.
        email = EmailSender()
        email.send("Hi, your order was places succesfully and will be with you within 2-5 working days")

order = Order()
order.create() """

 # Refactoring
"""
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email: {message}")

class MobileService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending text message: {message}")

class Order:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create(self):
        #Perform order creation logic, e.g. validate order details check producto stock, save to db etc.
        self.notification_service.send_notification("Hi, your order was places succesfully and will be with you within 2-5 working days")
 
order = Order(MobileService())
order.create()

order2 = Order(EmailService())
order2.create() """

# Composition - involves creating complex objects by combining simpler objects or components.

class Engine:
    def start(self):
        print(f"Engine starting")

class Wheels:
    def rotate(self):
        print(f"Rotate wheels")

class Chassis:
    def support(slef):
        print(f"Chassis is supporting car")

class Seats:
    def sit(slef):
        print(f"Sitting on seats")

class Car:
    def __init__(self):
        self._engine = Engine()
        self._wheels = Wheels()
        self._chassis = Chassis()
        self._seats = Seats()

    def start(self):
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        print("Car started")

car = Car()
car.start()


