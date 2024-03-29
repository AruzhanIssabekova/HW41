import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")

    while True:
        guess = int(input("Угадай число от 1 до 100 : "))
        attempts += 1

        if guess < number:
            print("Число больше.")
        elif guess > number:
            print("Число меньше.")
        else:
            print(f"Число верно.")
            break

guess_number()
