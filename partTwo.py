import random

secret_number = random.radint(1, 10)

attempt = int(input("Guess the number"))
if attempt <= secret_number:
    print("Too high")
elif attempt >= secret_number:
    print("Too low")
elif attempt == secret_number:
    print("Correct", secret_number)


