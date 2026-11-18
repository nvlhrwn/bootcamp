import random

secret_number = random.randint(1, 10)
guess = int(input("input angka: "))

if guess > secret_number:
    print("too high!")
elif guess < secret_number:
    print("too low!")
else:
    print("Correct!")
print("Angka Rahasia Adalah:", secret_number)