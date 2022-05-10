import random
import prompt


def play_brain_even():
    n = random.randrange(100)
    print('Question: ', n)
    answer = prompt.string('Your answer: ')
    answer.lower()

    # Определеяем правильный ответ
    correct_answer = ''
    if n % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    # Если ответ правильный:
    global yes_count
    if answer == correct_answer:
        print('Correct!')
        yes_count += 1
        if yes_count == 3:
            print(f'Contgratulations, {name}!')
            yes_count = 0
            play_brain_even()
        else:
            play_brain_even()

    # Если ответ неправильный:
    else:
        print(f"'{answer}', is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        yes_count = 0
        play_brain_even()


name = prompt.string('May I have your name? ')
print(f'Hello, {name}')
print('Answer "yes" if the number is even, otherwise answer "no".')
yes_count = 0
play_brain_even()
