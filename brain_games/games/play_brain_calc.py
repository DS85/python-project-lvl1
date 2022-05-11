import prompt
import random
from brain_games.games.game_logics import greeting, check_answer


def play_brain_calc():
    # Приветствие и начало игры
    greeting('What is the result of the expression?')
    rounds_count = 0
    yes_count = 0

    while rounds_count < 3:
        rounds_count += 1

        # Генерируем случайные значения для вопроса
        n1 = random.randint(0, 10)
        n2 = random.randint(0, 10)
        operation = random.choice('+-*')

        # Определеяем правильный ответ
        correct_answer = 0
        if operation == '+':
            correct_answer = n1 + n2
        elif operation == '-':
            correct_answer = n1 - n2
        elif operation == '*':
            correct_answer = n1 * n2

        # Задаем вопрос и получаем ответ
        print(f'Question: {n1} {operation} {n2}')
        answer = prompt.string('Your answer: ')
        answer.lower()

        # Обрабатываем ответ
        yes_count, rounds_count = check_answer(
            answer, correct_answer, yes_count, rounds_count)
