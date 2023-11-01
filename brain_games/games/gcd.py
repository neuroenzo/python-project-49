import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def check_gcd(number1: int, number2: int) -> str:
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1

    return str(number1 + number2)


def get_question_and_answer() -> tuple:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f'{number1} {number2}'
    answer = check_gcd(number1, number2)

    return question, answer
