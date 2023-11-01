import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer() -> tuple:
    start_number = random.randint(1, 100)
    step = random.randint(2, 9)
    dots = '..'
    progression = []

    count = 0
    while count < 10:
        start_number += step
        progression.append(start_number)

        count += 1

    answer = progression[step]
    progression[step] = dots
    question = " ".join(map(str, progression))

    return question, str(answer)
