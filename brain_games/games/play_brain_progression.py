import prompt
import random
from brain_games.games.game_logics import greeting, check_answer


def play_brain_progression():
    # Приветствие и начало игры
    greeting('What number is missing in the progression?')
    rounds_count = 0
    yes_count = 0

    while rounds_count < 3:
        rounds_count += 1

        # Генерируем случайные значения для вопроса
        start = random.randint(0, 1)
        step = random.randint(2, 5)
        stop = start + step * 10
        hidden_i = random.randint(0, 9)
        seq = list(range(start, stop, step))

        # Определеяем правильный ответ
        correct_answer = seq[hidden_i]
        seq[hidden_i] = '...'

        # Задаем вопрос и получаем ответ
        print('Question:', *seq)
        answer = prompt.string('Your answer: ')

        # Обрабатываем ответ
        yes_count = check_answer(answer, correct_answer, yes_count)
