import random
import string

def generator_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
    try:
       password_length = int(input("Enter the desired length of the password: "))
       if password_length <= 0:
           print("Invalid password length. Please enter a positive integer.")
       else:
        generated_password = generator_password(password_length)
        print(f"Generated Password: {generated_password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
