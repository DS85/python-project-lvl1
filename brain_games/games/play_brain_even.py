import random
import prompt
from brain_games.games.game_logics import *


def play_brain_even():
    # Приветствие и начало игры
    name = greeting('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_count = 0
    yes_count = 0

    while rounds_count < 3:
        rounds_count += 1

        # Генерируем случайные значения для вопроса
        n = random.randrange(100)

        # Определеяем правильный ответ
        correct_answer = ''
        if n % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        # Задаем вопрос и получаем ответ
        print('Question: ', n)
        answer = prompt.string('Your answer: ')
        answer.lower()

        # Обрабатываем ответ
        yes_count = check_answer(answer, correct_answer, yes_count)
