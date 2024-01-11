#Password_Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a valid positive length.")
            else:
                return length

        except ValueError:
            print("Please enter a valid integer for the password length.")

def main():
    length = get_password_length()
    password = generate_password(length)
    print("Generated Password:", password)
main()   