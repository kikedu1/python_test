# Single Responsibility Principle (SRP)

# A class should have only one reason to change, meaning that it should hae only one responsibility purpose.

class EmailSender:
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def register(self):
        print("Registering user {self.username}")

        email_sender = EmailSender()
        email_sender.send(self.email, f"Welcome to our platform {self.username}")

user = User("danteman", "dan@gmail.com")
user.register()      