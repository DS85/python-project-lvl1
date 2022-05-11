import prompt
import random
from brain_games.games.game_logics import greeting, check_answer


def play_brain_gcd():
    # Приветствие и начало игры
    greeting('Find the greatest common divisor of given numbers.')
    rounds_count = 0
    yes_count = 0

    while rounds_count < 3:
        rounds_count += 1

        # Генерируем случайные значения для вопроса
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)

        # Определеяем правильный ответ
        correct_answer = 0
        if n1 > n2:
            n = n1
        else:
            n = n2
        while True:
            if n1 % n == 0 and n2 % n == 0:
                correct_answer = n
                break
            else:
                n -= 1

        # Задаем вопрос и получаем ответ
        print(f'Question: {n1} {n2}')
        answer = prompt.string('Your answer: ')

        # Обрабатываем ответ
        yes_count, rounds_count = check_answer(answer, correct_answer, yes_count, rounds_count)
