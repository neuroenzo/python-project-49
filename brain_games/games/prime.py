import random

DESCRIPTION = 'Answer "yes" if given number is prime.' \
              ' Otherwise answer "no".'


def get_question_and_answer() -> tuple:
    number = random.randint(2, 100)
    question = number

    divider = 2
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            divider += 1

    answer = 'no' if divider > 2 else 'yes'

    return question, answer
