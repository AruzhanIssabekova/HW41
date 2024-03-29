import random

def choose_word():
    words = ["яблоко", "банан", "апельсин", "клубника", "виноград", "ананас"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Добро пожаловать в игру 'Виселица'!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Угадай букву: ").lower()
        if guess in guessed_letters:
            print("Это буква уже была!")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
            if "_" not in display_word(word, guessed_letters):
                print("Ты угадал.")
                break
        else:
            attempts -= 1
            print(f"Неверно! Утебя есть {attempts} попытки.")

    if attempts == 0:
        print(f"Ты проиграл. Слово было '{word}'.")

hangman()
