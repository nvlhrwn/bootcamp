import random

choice_level = int(input("Pilih level 1-3): "))
if choice_level == 1:
   max_number = 10
elif choice_level == 2:
    max_number = 50
else:
    max_number = 100

secret_number = random.randint(1, max_number)
guess = 0
while guess != secret_number:
    guess = int(input(f"Tebak angka antara 1 - {max_number}: "))

    if guess > secret_number:
        print("too high!")
    elif guess < secret_number:
        print("too low!")
    else:
        print("Correct!")
print("Angka Rahasia Adalah:", secret_number)