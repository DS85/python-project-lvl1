import prompt
import random
from brain_games.games.game_logics import greeting, check_answer


def play_brain_prime():
    # Приветствие и начало игры
    greeting('Answer "yes" if given number is prime. Otherwise answer "no".')
    rounds_count = 0
    yes_count = 0

    while rounds_count < 3:
        rounds_count += 1

        # Генерируем случайные значения для вопроса
        n = random.randint(2, 30)

        # Определеяем правильный ответ
        d = 2
        while n % d != 0:
            d += 1
        if d != n:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        # Задаем вопрос и получаем ответ
        print('Question:', n)
        answer = prompt.string('Your answer: ')
        answer.lower()

        # Обрабатываем ответ
        yes_count = check_answer(answer, correct_answer, yes_count)
