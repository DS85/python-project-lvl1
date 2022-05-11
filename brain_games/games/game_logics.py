import prompt


def greeting(string):
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(string)
    return name


def check_answer(answer, correct_answer, yes_count):
    global name
    # Если ответ правильный
    if str(answer) == str(correct_answer):
        print('Correct!')
        yes_count += 1
        if yes_count == 3:
            print(f'Congratulations, {name}!')
            return yes_count
        else:
            return yes_count

    # Если ответ неправильный:
    else:
        print(f"'{answer}', is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        return yes_count
