import random
import string

# Show welcome message
print(" Welcome to the Password Generator!")

# Step 1: Ask user for desired password length
try:
    length = int(input("Enter the password length: "))

    if length <= 0:
        print(" Password length must be greater than 0.")
    else:
        # Step 2: Define possible characters (uppercase, lowercase, digits, symbols)
        characters = string.ascii_letters + string.digits + string.punctuation

        # Step 3: Generate password using random.choice()
        password = ''.join(random.choice(characters) for _ in range(length))

        # Step 4: Display the generated password
        print(" Your secure password is:", password)

except ValueError:
    print(" Please enter a valid number.")
