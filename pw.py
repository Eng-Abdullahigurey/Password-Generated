import random

# Character sets
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()+-=[]{}/?<>|'~'"

# Combine all character sets
all_characters = lowercase + uppercase + numbers + symbols

# Password generator function
def password_generator(length):
    password = ""
    for i in range(length):
        password += random.choice(all_characters)
    return password

# User interaction
print("Welcome to the password generator!")
print("You can generate a password with the length you want:")

try:
    user_length = int(input("Enter password length: "))
    if user_length <= 0:
        print("Password length must be greater than 0.")
    else:
        generated_password = password_generator(user_length)
        print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")
