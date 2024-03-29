import random


def greet_player():
    print("Добро пожаловать в игре камень, ножницы, бумага!")


def get_player_choice():
    while True:
        choice = input("Сделайте ход(камень, ножницы, бумага): ").lower()
        if choice in ['камень', 'ножницы', 'бумага']:
            return choice
        else:
            print("Неверный ход.")


def get_random_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])
def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья!"
    elif (player_choice == 'каимнь' and computer_choice == 'ножницы') or \
            (player_choice == 'ножницы' and computer_choice == 'бумага') or \
            (player_choice == 'бумага' and computer_choice == 'камень'):
        return "Победа!"
    else:
        return "Поражение."


def play_again():
    return input("Хотите сыграть снова? (да/нет): ").lower() == 'да'


if __name__ == "__main__":
    greet_player()

    while True:
        player_choice = get_player_choice()
        computer_choice = get_random_computer_choice()

        print(f"Твой ход: {player_choice}")
        print(f"Ход компьютера: {computer_choice}")

        result = check_winner(player_choice, computer_choice)
        print(result)

        if not play_again():
            break
