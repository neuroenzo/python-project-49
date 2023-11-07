import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer() -> tuple:
    start_number = random.randint(1, 100)
    step = random.randint(2, 9)

    progression_length = 10
    progression = list(range(
        start_number,
        start_number + (step * progression_length),
        step)
    )

    answer = progression[step]
    progression[step] = '..'
    question = " ".join(map(str, progression))

    return question, str(answer)
