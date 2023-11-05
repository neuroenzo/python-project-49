import random

DESCRIPTION = 'Answer "yes" if given number is prime.' \
              ' Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            divider += 1

    if divider <= 2:
        return True
    else:
        return False


def get_question_and_answer() -> tuple:
    number = random.randint(1, 100)
    question = number

    divider = is_prime(number)

    answer = 'yes' if divider else 'no'

    return question, answer
