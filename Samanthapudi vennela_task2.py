import random
import string

class PasswordGenerator:

    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate_password(self, length):
        all_characters = (
            self.lowercase +
            self.uppercase +
            self.digits +
            self.symbols
        )

        password = []

        password.append(random.choice(self.lowercase))
        password.append(random.choice(self.uppercase))
        password.append(random.choice(self.digits))
        password.append(random.choice(self.symbols))

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        return "".join(password)


def main():
    print("=" * 50)
    print("      ADVANCED PASSWORD GENERATOR")
    print("=" * 50)

    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4")
        return

    generator = PasswordGenerator()

    password = generator.generate_password(length)

    print("\nGenerated Password:")
    print(password)

    print("\nPassword Strength Analysis")
    print("-" * 30)

    strength = 0

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in string.punctuation for c in password):
        strength += 1

    if length >= 12:
        strength += 1

    if strength <= 2:
        print("Weak Password")
    elif strength <= 4:
        print("Medium Password")
    else:
        print("Strong Password")


if __name__ == "__main__":
    main()