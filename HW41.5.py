def quiz():
    questions = {
        "Столица Германии.": "Берлин",
        "Страна восходящего солнца.": "Япония",
        "Самая длинная река.": "Нил",
        "Где появился человек?":"Кения"
    }
    score = 0

    print("Добро пожаловать в Векторину!")
    print("Ответ пишите лдним словом.")

    for question, answer in questions.items():
        user_answer = input(question + " ").strip().capitalize()
        if user_answer == answer:
            print("Верно!")
            score += 1
        else:
            print(f"Неверно! Ответ: {answer}.")

    print(f"Балл: {score} из {len(questions)}.")

quiz()
